"""Nox sessions."""
import os
import shlex
import shutil
import sys
from pathlib import Path
from textwrap import dedent

import nox

try:
    from nox_poetry import Session
    from nox_poetry import session
except ImportError:
    message = f"""\
    Nox failed to import the 'nox-poetry' package.

    Please install it using the following command:

    {sys.executable} -m pip install nox-poetry"""
    raise SystemExit(dedent(message)) from None


package = "price_series_calc"
python_versions = ["3.10", "3.9", "3.8", "3.7"]
nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "tests",
    "docs",
)


@session(python=python_versions)
def tests(session: Session) -> None:
    """Run the test suite."""
    session.install(".")
    session.install("coverage[toml]", "pytest", "pygments")
    try:
        session.run("coverage", "run", "--parallel", "-m", "pytest", *session.posargs)
    finally:
        if session.interactive:
            session.notify("coverage", posargs=[])


@session(python=python_versions[0])
def coverage(session: Session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["report"]

    session.install("coverage[toml]")

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)


@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["-W", "-n", "docs", "docs/_build"]

    if session.interactive and not session.posargs:
        args = ["-a", "--watch=docs/_static", "--open-browser", *args]

    builddir = Path("docs_bak", "_build")
    if builddir.exists():
        shutil.rmtree(builddir)

    session.install("-r", "docs/requirements.txt")

    if session.interactive:
        session.run("sphinx-autobuild", *args)
    else:
        session.run("sphinx-build", *args)


@nox.session
def linkcheck(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["-b", "linkcheck", "-W", "--keep-going", "docs", "docs/_build"]

    builddir = Path("docs_bak", "_build")
    if builddir.exists():
        shutil.rmtree(builddir)

    session.install("-r", "docs/requirements.txt")

    session.run("sphinx-build", *args)

