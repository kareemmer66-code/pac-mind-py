"""Beginner launcher: create a local virtual environment, install, then open the game.

Run this with the Python installed on your computer. The project environment is
isolated in .venv; no global Python packages or administrator privileges are needed.
"""

import argparse
import hashlib
import os
import subprocess
import sys
import venv
from pathlib import Path

MINIMUM_PYTHON = (3, 10)


def prepare_environment(project: Path) -> Path:
    environment = project / ".venv"
    executable = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not executable.exists():
        print("Creating the project's Python environment...", flush=True)
        venv.EnvBuilder(with_pip=True).create(environment)

    requirements = project / "requirements.txt"
    expected = hashlib.sha256(requirements.read_bytes()).hexdigest()
    stamp = environment / ".pacmind-requirements"
    installed = stamp.read_text() if stamp.exists() else ""
    if installed != expected:
        print(
            "Installing Pygame Community Edition (internet needed on first launch)...",
            flush=True,
        )
        subprocess.run(
            [str(executable), "-m", "pip", "install", "-r", str(requirements)], check=True
        )
        stamp.write_text(expected)
    return executable


def main() -> int:
    parser = argparse.ArgumentParser(description="Set up and run PAC-MIND")
    parser.add_argument(
        "--check", action="store_true", help="Verify installation without opening the game."
    )
    arguments = parser.parse_args()
    if sys.version_info[:2] < MINIMUM_PYTHON:
        print("PAC-MIND needs Python 3.10 or newer. Python 3.12 is recommended.")
        return 1
    project = Path(__file__).resolve().parent
    try:
        executable = prepare_environment(project)
        if arguments.check:
            subprocess.run(
                [
                    str(executable),
                    "-c",
                    "import pygame; print('PAC-MIND dependencies are ready.')",
                ],
                check=True,
            )
            return 0
        return subprocess.call([str(executable), "-m", "pacmind"], cwd=project)
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"Setup failed: {error}")
        print("Check your Python installation and internet connection, then run again.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
