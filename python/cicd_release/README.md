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

In the repo, create a directory named `~/.github/workflows` if it doesn't already exist. 

**Important note:** This is **not** `~/mwe/python/cicd_release/.github/workflows` directory.

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
          # GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
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
          # GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
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
# for example, with v0.0.4
git tag -a v0.0.4 -m 'fouth release'
git push origin v0.0.4
```

This workflow will:

* Trigger on a new tag push that matches the pattern `v*.*.*`.
* Check out the code.
* Set up Python.
* Install dependencies using pip.
* Build the project using `python -m build`.
* Create a GitHub release with the tag name and upload the built assets.

Make sure the `pyproject.toml` is correctly configured for building the project.
The build package will use the information in `pyproject.toml` to create the distribution files.

### Permissions Troubleshooting

The error "Resource not accessible by integration" typically occurs when the GitHub Actions workflow is trying to perform an action that requires higher permissions than those granted by the default `GITHUB_TOKEN`. This can happen, for example, when trying to create a release, push code, or interact with other repositories.

Make sure that the `GITHUB_TOKEN` has the necessary permissions. By default, the `GITHUB_TOKEN` has read and write permissions for the repository where the workflow is running. However, if you need to interact with other repositories or perform actions that require higher permissions, you may need to create a personal access token (PAT) with the required scopes.

If the default `GITHUB_TOKEN` does not have sufficient permissions, you can create a PAT and use it in your workflow:

* Go to your GitHub account.
* Navigate to "Settings" > "Developer settings" > "Personal access tokens".
* Click "Generate new token".
* Select the necessary scopes (e.g., both repo and workflow should be checked).
* Generate the token and copy it.

Add the PAT to Repository Secrets:

* Navigate to the repository on GitHub.  
* Click on the "Settings" tab in the repository.
* Navigate to Secrets and Variables:
  * In the left sidebar, click on "Secrets and variables" and then "Actions."
  * Add a New Secret:
  * Click "New repository secret."
  * Name the secret (e.g., `PERSONAL_ACCESS_TOKEN`).
  * Paste the PAT and save it.

## Optional: Manually build wheel file

To build a .whl file:

```bash
# Assure `setuptools` and `wheel` are installed and upgraded
 pip install --upgrade pip setuptools
pip install build

# Create the .whle file
cd ~/mwe/python/cicd_release (path contains the pyproject.toml file)
python -m build

# Verify the .whl file is built to ~/mwe/python/cicd_release/dist/
# example: cicd_example-0.0.8-py3-none-any.whl
```
