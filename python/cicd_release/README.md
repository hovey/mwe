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

### Automated Release

Use GitHub Actions, which allows the developer to automate workflows directly in 
the GitHub repository.

In the repo, create a directory named `~/mwe/python/cicd_release/.github/workflows` if it doesn't already exist. 
Inside this directory, create a file named `release.yml` (or any name you prefer):

```bash
name: Create Release

on:
  push:
    tags:
      - 'v*.*.*'  # This pattern matches tags like v1.0.0, v2.1.3, etc.

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'  # Specify the Python version you need

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build

      - name: Build the project
        run: python -m build

      - name: Create GitHub Release
        id: create_release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          body: |
            Automatic release for version ${{ github.ref }}.
          draft: false
          prerelease: false

      - name: Upload Release Asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }}
          asset_path: ./dist/*.tar.gz
          asset_name: myproject-${{ github.ref }}.tar.gz
          asset_content_type: application/gzip
```

Commit and push the `release.yml` file to the repository.

```bash
git add .github/workflows/release.yml
git commit -m "add github actions"
git push origin main
```

Create a new tag and push it to trigger the workflow.

```bash
git tag -a v0.0.4 -m 'fouth release'
git push origin v0.0.4
```

This workflow will:

* Trigger on a new tag push that matches the pattern v*.*.*.
* Check out the code.
* Set up Python.
* Install dependencies using pip.
* Build the project using `python -m build`.
* Create a GitHub release with the tag name and upload the built assets.

Make sure the `pyproject.toml` is correctly configured for building the project.
The build package will use the information in `pyproject.toml` to create the distribution files.
