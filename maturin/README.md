# maturin

Maturin is a build system for Rust and Python.  Maturin allows for building and publishing of Rust crates with pyo3, cffi and uniffi.  With Maturin for Python, it allows for building of wheels for Python 3.8+ on Windows, macOS, and Linux.

## Introduction

We recreate the [Maturin Tutorial](https://www.maturin.rs/tutorial), which demonstrates how to create a Rust command line application and wrap it using pyo3 so that the game can be run from Python.

```bash
cd ~/mwe
mkdir maturin
cd maturin
python3.11 -m venv .venv
source .venv/bin/activate.fish
pip install --upgrade pip
pip install maturin

pip list

Package    Version
---------- -------
maturin    1.6.0
pip        24.1.1
setuptools 65.5.0

cargo new --lib --edition 2021 guessing-game

# the following structure is created:
guessing-game/
├── Cargo.toml
└── src
    └── lib.rs
```

Create the [pyproject.toml](guessing-game/pyproject.toml).

Instead of creating a `bin` crate, as in the The Rust Book example, we create a `lib` crate here in Rust, and then expose the main logic as a Python function.  Update the [src/lib.rs](guessing-game/src/lib.rs) file.

Starting with the code from The Rust Book, three modification were made:

1. Include the pyo3 prelude,
2. Add `#[pyfunction]` to `guess_the_number` function, and
3. Add the `#[pymodule]` block to expose the function as part of a Python module.

This is just a Rust project at this point.  One can expect to build the project using `cargo build`.  The `maturin` adds some platform-specific build configuration and creates a binary result as a wheel (`.whl`) file.  A wheel file is an archieve of compiled components suited for for installation with `pip`, the Python package manager.

```bash
(.venv)  ~/mwe/maturin/guessing-game> maturin develop
🔗 Found pyo3 bindings with abi3 support for Python ≥ 3.8
🐍 Not using a specific python interpreter
📡 Using build options features from pyproject.toml
   Compiling target-lexicon v0.12.14
   Compiling libc v0.2.155
   Compiling once_cell v1.19.0
   Compiling autocfg v1.3.0
   Compiling proc-macro2 v1.0.86
   Compiling cfg-if v1.0.0
   Compiling unicode-ident v1.0.12
   Compiling parking_lot_core v0.9.10
   Compiling heck v0.4.1
   Compiling scopeguard v1.2.0
   Compiling smallvec v1.13.2
   Compiling portable-atomic v1.6.0
   Compiling ppv-lite86 v0.2.17
   Compiling unindent v0.2.3
   Compiling indoc v2.0.5
   Compiling lock_api v0.4.12
   Compiling memoffset v0.9.1
   Compiling quote v1.0.36
   Compiling syn v2.0.68
   Compiling getrandom v0.2.15
   Compiling pyo3-build-config v0.21.2
   Compiling rand_core v0.6.4
   Compiling parking_lot v0.12.3
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling pyo3-ffi v0.21.2
   Compiling pyo3 v0.21.2
   Compiling pyo3-macros-backend v0.21.2
   Compiling pyo3-macros v0.21.2
   Compiling guessing-game v0.1.0 (/Users/chovey/mwe/maturin/guessing-game)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 7.06s
📦 Built wheel for abi3 Python ≥ 3.8 to /var/folders/87/_m6404ms1hd30kz498l9bt8w002wpg/T/.tmpTddTjK/guessing_game-0.1.0-cp38-abi3-macosx_11_0_arm64.whl
✏️  Setting installed package as editable
🛠 Installed guessing-game-0.1.0
(.venv)  ~/mwe/maturin/guessing-game> pip list

Package       Version Editable project location
------------- ------- ---------------------------------------
guessing-game 0.1.0   /Users/chovey/mwe/maturin/guessing-game
maturin       1.6.0
pip           24.1.1
setuptools    65.5.0
(.venv)  ~/mwe/maturin/guessing-game>
```

Now, run the program:

```bash
python
>>> import guessing_game
>>> guessing_game.guess_the_number()
Guess the number!
Please input your guess.
42
You guessed: 42
Too small!
Please input your guess.
80
You guessed: 80
Too small!
Please input your guess.
90
You guessed: 90
Too big!
Please input your guess.
85
You guessed: 85
Too big!
Please input your guess.
83
You guessed: 83
You win!
>>>
```

## Reference

* [Matiurin User Guide](https://www.maturin.rs)
* [Maturing Tutorial Guessing Game](https://www.maturin.rs/tutorial)
