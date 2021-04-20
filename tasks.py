import os
from pathlib import Path
from shutil import which
import sys

from invoke import task

PKG_NAME = "jinja_filters"
PKG_PATH = Path(f"pelican/plugins/{PKG_NAME}")

BIN_DIR = "bin" if os.name != "nt" else "Scripts"
ACTIVE_VENV = os.environ.get("VIRTUAL_ENV", None)
VENV_HOME = Path(os.environ.get("WORKON_HOME", "~/virtualenvs")).expanduser()
VENV_PATH = Path(ACTIVE_VENV) if ACTIVE_VENV else (VENV_HOME / PKG_NAME)
VENV = str(VENV_PATH.expanduser())
VENV_BIN = Path(VENV) / Path(BIN_DIR)
POETRY = which("poetry") if which("poetry") else (VENV_BIN / "poetry")
PRECOMMIT = which("pre-commit") if which("pre-commit") else f"{POETRY} run pre-commit"
DEFAULT_PYTHON = which("python") if which("python") else None

TOOLS = ["poetry", "pre-commit"]


@task
def tests(c):
    """Run the test suite"""
    PTY = True if os.name != "nt" else False
    c.run(f"{POETRY} run pytest", pty=PTY)


@task
def black(c, check=False, diff=False):
    """Run Black auto-formatter, optionally with --check or --diff"""
    check_flag, diff_flag = "", ""
    if check:
        check_flag = "--check"
    if diff:
        diff_flag = "--diff"
    c.run(f"{POETRY} run black {check_flag} {diff_flag} {PKG_PATH} tasks.py")


@task
def isort(c, check=False, diff=False):
    check_flag, diff_flag = "", ""
    if check:
        check_flag = "-c"
    if diff:
        diff_flag = "--diff"
    c.run(f"{POETRY} run isort {check_flag} {diff_flag} .")


@task
def flake8(c):
    c.run(f"{POETRY} run flake8 {PKG_PATH} tasks.py")


@task
def lint(c):
    isort(c, check=True)
    black(c, check=True)
    flake8(c)


@task
def tools(c):
    """Install tools in the virtual environment if not already on PATH"""
    for tool in TOOLS:
        if not which(tool):
            if ACTIVE_VENV:
                print(f"** Installing {tool} into virtual environment")
                c.run(f"{VENV_BIN}/pip install {tool}")
            else:
                print(f"** Installing {tool} with poetry")
                c.run(f"{POETRY} run pip install {tool}")


@task
def precommit(c):
    """Install pre-commit hooks to .git/hooks/pre-commit"""
    print("** Installing pre-commit hooks")
    c.run(f"{PRECOMMIT} install")


@task
def setup(c):
    """Run this to get your development environment set up"""
    if which("poetry") or ACTIVE_VENV:
        tools(c)
        c.run(f"{POETRY} run python -m pip install pip --upgrade")
        c.run(f"{POETRY} install")
        precommit(c)
    else:
        sys.exit(
            """Poetry is not installed, and there is no active virtual environment
            available. You can either manually create and activate a virtual
            environment, or you can install Poetry via:

            curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

            Once you have taken one of the above two steps, run `invoke setup` again.
            """
        )
