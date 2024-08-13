# CI/CD Release

Minimum working examle of a release of a Python library with automated CI/CD.

## Install

```bash
cd ~/mwe/python/cicd_release
python3.11 -m venv .venv

# Activate the venv with one of the following:
source .venv/bin/activate       # for bash shell
source .venv/bin/activate.csh   # for c shell
source .venv/bin/activate.fish  # for fish shell
.\.venv\Scripts\activate        # for powershell

pip install --upgrade pip setuptools

pip install -e .
```

### Run

```bash
# run the command line entry point
cicd_example
-------------------------------
This is the cicd_example module
-------------------------------

cicd_example
    (this command)

hello
    Runs the 'Hello world!' example.

pytest
    Runs the test suite (non-verbose option).

pytest -v
    Runs the test suite (verbose option).
```

### Test

```bash
# run the tests
pytest -v

===================================================== test session starts =====================================================
platform darwin -- Python 3.11.9, pytest-8.3.2, pluggy-1.5.0 -- /Users/chovey/mwe/python/cicd_release/.venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/chovey/mwe/python/cicd_release
configfile: pyproject.toml
collected 1 item                                                                                                              

tests/test_command_line.py::test_hello_world PASSED                                                                     [100%]

====================================================== 1 passed in 0.02s ======================================================
```

### Create a Tag

The distribution steps will tag the code state as a release version, with a semantic version number, build the code as a wheel file, and publish to the wheel file as a release to GitLab.

View existing tags, if any:

```bash
git tag
```

Create a tag.  Tags can be lightweight or annotated.
Annotated tags are recommended since they store tagger name, email, date, and
message information.  Create an annotated tag:

```bash
# example of an annotated tag
git tag -a v0.0.1 -m "Release version 0.0.1"
```

Push the tag to the repository:

```bash
# example continued
git push origin v0.0.1
```