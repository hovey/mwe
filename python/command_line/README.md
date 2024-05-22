# command line entry points

```bash
pip install --upgrade setuptools
```

Create a [`pyproject.toml`](pyproject.toml) file.  Organize the project folder as follows:

```bash
mypackage
├── pyproject.toml  # and/or setup.cfg/setup.py (depending on the configuration method)
|   # README.rst or README.md (a nice description of your package)
|   # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
|   # MANIFEST.in (to include specific files, e.g., data files, with distribution)
└── mypackage
    ├── __init__.py
    └── ... (other Python files)
```

```bash
pip install --upgrade build
```

Create a distribution (e.g. a tar.gz file and a .whl file in the dist directory), which can be uploaded to PyPI!

```bash
python -m build
```

## Developer install

> setuptools allows you to install a package without copying any files to your interpreter directory (e.g. the site-packages directory). This allows you to modify your source code and have the changes take effect without you having to rebuild and reinstall. Here’s how to do it:

```bash
pip install --editable .
```

Example:

```bash
# before editable install
(.venv)  (main) chovey@s1088757/Users/chovey/mwe/python/command_line> pip list
Package         Version
--------------- -------
build           1.2.1
packaging       24.0
pip             24.0
pyproject_hooks 1.1.0
setuptools      70.0.0

# install developer mode
pip install --editable .

# after editable install
(.venv)  (main) chovey@s1088757/Users/chovey/mwe/python/command_line> pip list
Package            Version  Editable project location
------------------ -------- -------------------------------------
build              1.2.1
certifi            2024.2.2
charset-normalizer 3.3.2
idna               3.7
importlib_metadata 7.1.0
mypackage          0.0.1    /Users/chovey/mwe/python/command_line
packaging          24.0
pip                24.0
pyproject_hooks    1.1.0
requests           2.32.2
setuptools         70.0.0
urllib3            2.2.1
zipp               3.18.2
```

## The command line interface

```bash
(.venv)  (main) chovey@s1088757/Users/chovey/mwe/python/command_line> mypackage
----------------------------
This is the mypackage module
----------------------------

mypackage
    (this command)

hello
    Runs the 'Hello World!' example.

pytest
    Runs the test suite (non-verbose option).

pytest -v
    Runs the test suite (verbose option).

(.venv)  (main) chovey@s1088757/Users/chovey/mwe/python/command_line> 
```

## References

* [setuptools quickstart](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
