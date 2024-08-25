#!/usr/bin/env python3
import json
import sys
import os
import argparse

def load_programs_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON in file '{file_path}'.", file=sys.stderr)
        return None

def get_program_names(programs_data):
    return [program['command'][0] for program in programs_data]

def filter_terminals(programs_data):
    terminal_names = ['alacritty', 'gnome-terminal']  # Add more terminal names as needed
    return [
        program for program in programs_data
        if any(term in program['command'][0].lower() for term in terminal_names)
    ]

def create_cmd_json(filtered_programs, output_path):
    cmd_data = {}
    for i, program in enumerate(filtered_programs, 1):
        cmd_data[f"terminal{i}"] = {
            "command": program['command'],
            "working_directory": program['working_directory'],
            "run_in_terminal": ""  # Empty string for users to fill in later
        }
    with open(output_path, 'w') as f:
        json.dump(cmd_data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(
        description="Generate workspace_[WORKSPACE NUMBER]_cmd.json by detecting workspace_[WORKSPACE NUMBER]_programs.json in directory [DIRECTORY], and saving it in directory [DIRECTORY]"
    )
    parser.add_argument("-w", "--workspace", type=int, required=True, metavar="WORKSPACE NUMBER", help="Workspace number")
    parser.add_argument("-d", "--directory", type=str, required=True, help="Directory containing the programs.json file and where cmd.json will be saved")
    args = parser.parse_args()

    input_file = os.path.join(args.directory, f"workspace_{args.workspace}_programs.json")
    output_file = os.path.join(args.directory, f"workspace_{args.workspace}_cmd.json")

    programs_data = load_programs_json(input_file)
    if programs_data is None:
        sys.exit(1)

    all_programs = get_program_names(programs_data)
    filtered_programs = filter_terminals(programs_data)

    # Print informative output in a readable format
    print("Detected Programs:")
    for program in all_programs:
        print(f"  - {program}")

    print("\nFiltered Programs (Terminals):")
    for program in filtered_programs:
        print(f"  - {program['command'][0]}")

    create_cmd_json(filtered_programs, output_file)
    print(f"\ncmd.json created at: {output_file}")
    print("You can now edit the 'run_in_terminal' field in the cmd.json file to specify commands to run in each terminal.")

if __name__ == "__main__":
    main()
