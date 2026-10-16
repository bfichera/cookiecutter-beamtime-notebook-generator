from pathlib import Path
from subprocess import run


venv = Path("workflow") / "envs" / "venv"
run(["/usr/bin/env", "python", "-m", "venv", str(venv)], check=True)
run(
    [
        str(venv / "bin" / "python"),
        "-m",
        "pip",
        "install",
        "jinja2",
        "jupytext",
    ],
    check=True,
)
