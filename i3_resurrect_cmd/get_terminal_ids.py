#!/usr/bin/env python3

import i3ipc
import sys

def get_terminal_windows(i3, workspace):
    terminal_windows = []
    for con in workspace.descendants():
        # Check if the window is a terminal. Add more terminal classes if needed.
        if con.window_class in ["Alacritty", "gnome-terminal"]:
            terminal_windows.append(con)
    return terminal_windows

def find_workspace_by_num(i3, workspace_num):
    workspaces = i3.get_workspaces()
    for ws in workspaces:
        if ws.num == workspace_num:
            return i3.get_tree().find_by_id(ws.ipc_data['id'])
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python get_terminal_ids.py <workspace_number>")
        sys.exit(1)

    workspace_num = int(sys.argv[1])

    i3 = i3ipc.Connection()
    workspace = find_workspace_by_num(i3, workspace_num)
    
    if not workspace:
        print(f"Workspace {workspace_num} not found")
        sys.exit(1)

    terminal_windows = get_terminal_windows(i3, workspace)
    
    if not terminal_windows:
        print(f"No terminal windows found in workspace {workspace_num}")
        sys.exit(1)

    print(f"Terminal windows in workspace {workspace_num}:")
    for i, window in enumerate(terminal_windows, 1):
        print(f"Terminal {i}: Window ID = {window.window}, Class = {window.window_class}")

if __name__ == "__main__":
    main()
