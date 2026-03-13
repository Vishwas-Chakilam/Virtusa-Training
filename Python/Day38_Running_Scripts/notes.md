# Day 38: Running Python Scripts

## The Interpreter
Python requires an interpreter to execute `.py` files.
- Command: `python myscript.py` or `python3 myscript.py`

## Command Line Arguments
Variables passed to the script during execution. Accessible via `sys.argv`.
- `sys.argv[0]` is the name of the script itself.
- `sys.argv[1]` ... `sys.argv[N]` are the arguments.

## Virtual Environments
A tool to keep dependencies required by different projects separate.
- Creation: `python -m venv myenv`
- Activation (Windows): `myenv\Scripts\activate`
- Activation (Unix/Mac): `source myenv/bin/activate`
