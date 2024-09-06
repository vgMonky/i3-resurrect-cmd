{ lib
, python3Packages
, fetchFromGitHub
, i3
, xdotool
, xorg
, i3-resurrect
}:

python3Packages.buildPythonApplication rec {
  pname = "i3-resurrect-cmd";
  version = "0.1.0-dev";

  src = fetchFromGitHub {
    owner = "vgMonky";
    repo = "i3-resurrect-cmd";
    rev = "v${version}";
    sha256 = "sha256-fVD7CEKaj864EcsEZ/gWITg9X1JuLQWelJajw0vyFHA="; 
  };

  propagatedBuildInputs = with python3Packages; [
    click
    i3ipc
  ];

  buildInputs = [
    i3
    xdotool
    xorg.xprop
    i3-resurrect
  ];

  meta = with lib; {
    description = "A command-line interface for i3-resurrect";
    homepage = "https://github.com/vgMonky/i3-resurrect-cmd";
    license = licenses.mit;  # Adjust if you're using a different license
    maintainers = with maintainers; [ vgMonky ];
  };
}
