#!/usr/bin/env python3
import json
import subprocess
import sys
import os
import argparse

def load_cmd_json(directory, workspace_number):
    file_path = os.path.join(directory, f"workspace_{workspace_number}_cmd.json")
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def get_terminal_ids(workspace_number):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    get_terminal_ids_script = os.path.join(script_dir, 'get_terminal_ids.py')
    result = subprocess.run([sys.executable, get_terminal_ids_script, str(workspace_number)],
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error getting terminal IDs: {result.stderr}")
        return []
    print("Debug: Output from get_terminal_ids.py:")
    print(result.stdout)
    terminal_ids = []
    for line in result.stdout.split('\n'):
        if "Window ID =" in line:
            parts = line.split()
            id_index = parts.index("=") + 1
            window_id = parts[id_index].rstrip(',')  # Remove trailing comma
            terminal_ids.append(int(window_id))
    print(f"Debug: Extracted terminal IDs: {terminal_ids}")
    return terminal_ids

def send_command(window_id, command):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    send_command_script = os.path.join(script_dir, 'send_command.py')
    subprocess.run([sys.executable, send_command_script, str(window_id), command])

def main():
    parser = argparse.ArgumentParser(description="Restore commands to terminals in a specified i3 workspace_number.")
    parser.add_argument("-w", "--workspace-number", type=int, required=True, 
                        help="The workspace_number to restore commands to.")
    parser.add_argument("-d", "--directory", type=str, required=True,
                        help="The directory where the workspace_[w]_cmd.json files are saved")
    args = parser.parse_args()

    workspace_number = args.workspace_number
    directory = args.directory

    cmd_data = load_cmd_json(directory, workspace_number)
    if not cmd_data:
        sys.exit(1)

    terminal_ids = get_terminal_ids(workspace_number)
    if not terminal_ids:
        print(f"No terminals found in workspace_number {workspace_number}")
        sys.exit(1)

    for i, (terminal_key, terminal_data) in enumerate(cmd_data.items()):
        if i >= len(terminal_ids):
            print(f"Warning: More terminals in cmd.json than found in workspace_number")
            break
        command = terminal_data.get('run_in_terminal', '').strip()
        if command:
            print(f"Executing in {terminal_key}: {command}")
            send_command(terminal_ids[i], command)
        else:
            print(f"No command specified for {terminal_key}")

if __name__ == "__main__":
    main()
