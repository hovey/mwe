# Virtual Environment

```bash
cd ~/my_project/path/
python -m venv .venv

# activate based on the shell
source .venv/bin/activate       # for bash shell
source .venv/bin/activate.csh   # for c shell
source .venv/bin/activate.fish  # for fish shell
.\.venv\Scripts\activate        # for powershell

# example

# prior to activation of the virtual environment
 (main) chovey@s1088757/Users/chovey/mwe/python/virtual_env>

# activate the virtual environment, the (.venv) shows on the command line
 (main) chovey@s1088757/Users/chovey/mwe/python/virtual_env> source .venv/bin/activate.fish
(.venv)  (main) chovey@s1088757/Users/chovey/mwe/python/virtual_env>

# optional: update pip
python -m pip install --upgrade pip

# deactivate the virtual environment, the (.venv) no longer appears on the command line
(.venv)  (main) chovey@s1088757/Users/chovey/mwe/python/virtual_env> deactivate
 (main) chovey@s1088757/Users/chovey/mwe/python/virtual_env>

# remove the virtual enivonnment
(main) chovey@s1088757/Users/chovey/mwe/python/virtual_env> rm -rf .venv
```

## References

* https://docs.python.org/3/library/venv.html

