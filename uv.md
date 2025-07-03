# UV

## Installation

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
wget -qO- https://astral.sh/uv/install.sh | sh

pipx install uv
pip install uv

cargo install --git https://github.com/astral-sh/uv uv

brew install uv
```

## Upgrading uv

```sh
uv self update
(pip install --upgrade pip)
pip install --upgrade uv
```

## Create a new project

https://docs.astral.sh/uv/guides/projects/#creating-a-new-project

```sh
mkdir hello-world
cd hello-world
uv init  # if no pyproject.toml exists

# if pyproject.toml already exists
uv venv # Create a virtual environment
uv pip install -e .[dev,torchless]
```

## Dependencies

```sh
uv add requests
# Specify a version constraint
uv add 'requests==2.31.0'

# Add a git dependency
uv add git+https://github.com/psf/requests

uv lock --upgrade-package requests

uv remove requests
```

## Uninstall

```code
uv cache clean
rm -r "$(uv python dir)"
rm -r "$(uv tool dir)"

rm ~/.local/bin/uv ~/.local/bin/uvx
```

