#!/usr/bin/env python3
import click
import subprocess
import sys
import os

@click.group()
def cli():
    pass

@cli.command()
@click.option('-w', '--workspace', type=int, required=True, help='Workspace number')
@click.option('-d', '--directory', type=str, required=True, help='Directory path')
def save(workspace, directory):
    """Save workspace and generate command JSON."""
    # Run original i3-resurrect save command
    subprocess.run(['i3-resurrect', 'save', '-w', str(workspace), '-d', directory], check=True)
    
    # Run your custom generate_cmd_json script
    generate_script = os.path.join(os.path.dirname(__file__), 'generate_cmd_json.py')
    subprocess.run([sys.executable, generate_script, '-w', str(workspace), '-d', directory], check=True)

@cli.command()
@click.option('-w', '--workspace', type=int, required=True, help='Workspace number')
@click.option('-d', '--directory', type=str, required=True, help='Directory path')
def restore(workspace, directory):
    """Restore workspace and send commands to terminals."""
    # Run original i3-resurrect restore command
    subprocess.run(['i3-resurrect', 'restore', '-w', str(workspace), '-d', directory], check=True)
    
    # Run your custom restore_cmd script
    restore_script = os.path.join(os.path.dirname(__file__), 'restore_cmd.py')
    subprocess.run([sys.executable, restore_script, '-w', str(workspace), '-d', directory], check=True)

if __name__ == '__main__':
    cli()
