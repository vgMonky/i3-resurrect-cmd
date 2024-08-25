# shell.nix

{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.virtualenv
    i3
    xdotool
    xorg.xprop
    i3-resurrect
  ];

  shellHook = ''
    # Create a virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
      virtualenv venv
    fi
    source venv/bin/activate

    # Install project dependencies
    pip install -e .

    # Set up environment variables
    export PYTHONPATH="$PWD:$PYTHONPATH"
  '';
}
