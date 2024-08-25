#!/usr/bin/env python3

import subprocess
import sys

def send_command_to_window(window_id, command):
    # Focus the window
    subprocess.run(['xdotool', 'windowactivate', '--sync', str(window_id)])
    
    # Type the command
    subprocess.run(['xdotool', 'type', command])
    
    # Press Enter
    subprocess.run(['xdotool', 'key', 'Return'])

def main():
    if len(sys.argv) != 3:
        print("Usage: python send_command.py <window_id> <command>")
        sys.exit(1)

    window_id = sys.argv[1]
    command = sys.argv[2]

    send_command_to_window(window_id, command)

if __name__ == "__main__":
    main()
