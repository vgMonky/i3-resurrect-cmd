{ lib
, python3Packages
, i3-resurrect
, xdotool
, xorg
}:

python3Packages.buildPythonApplication rec {
  pname = "i3-resurrect-cmd";
  version = "0.1.0";  # Update this as needed

  src = ./.;

  propagatedBuildInputs = with python3Packages; [
    click
    i3ipc
    i3-resurrect
    xdotool
    xorg.xprop
  ];

  doCheck = false;  # If you don't have tests set up yet

  meta = with lib; {
    description = "An extension for i3-resurrect that adds functionality for saving and restoring terminal commands";
    homepage = "https://github.com/vgMonky/i3-resurrect-cmd";  # Update with your actual GitHub URL
    license = licenses.mit;  # Adjust if you're using a different license
    maintainers = with maintainers; [ vgMonky ];  # Replace with your GitHub username
  };
}
