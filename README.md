# i3-resurrect-cmd

An extension for i3-resurrect that adds functionality for saving and restoring terminal commands.

## Installation

1. Ensure i3-resurrect is installed on your system.
2. Clone this repository.
3. Navigate to the repository directory.
4. Run `pip install -e .`

## Usage

- To save a workspace and generate command JSON:
  ```
  i3-resurrect-cmd save -w <workspace_number> -d <directory>
  ```

- To restore a workspace and send commands to terminals:
  ```
  i3-resurrect-cmd restore -w <workspace_number> -d <directory>
  ```

Replace <workspace_number> with the number of the workspace you want to save/restore, and <directory> with the path where you want to save the files.

## Development

This project uses a Nix shell for development. To enter the development environment:

1. Ensure you have Nix installed.
2. Run `nix-shell` in the project directory.

This will set up all necessary dependencies and create a Python virtual environment.
