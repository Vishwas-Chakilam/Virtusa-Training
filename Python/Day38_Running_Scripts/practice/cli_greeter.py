import sys

if len(sys.argv) > 1:
    print(f"Hello, {sys.argv[1]}")
else:
    print("Please provide a name argument. Usage: python cli_greeter.py [name]")