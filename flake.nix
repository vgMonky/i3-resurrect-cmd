{
  description = "A command-line interface for i3-resurrect";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        packages.default = pkgs.callPackage ./default.nix { };

        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            python3Packages.pip
            python3Packages.virtualenv
            python3Packages.click
            python3Packages.i3ipc
            i3
            xdotool
            xorg.xprop
            i3-resurrect
          ];
          shellHook = ''
            if [ ! -d "venv" ]; then
              virtualenv venv
            fi
            source venv/bin/activate
            pip install -e .
            export PYTHONPATH="$PWD:$PYTHONPATH"
          '';
        };
      }
    );
}
