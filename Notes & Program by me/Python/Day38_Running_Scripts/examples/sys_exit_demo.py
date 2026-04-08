import sys
# Exits code execution explicitly. 0 means success. Any >0 means error.
if len(sys.argv) < 2:
    print("Error: Missing argument.")
    sys.exit(1)
print("Argument valid:", sys.argv[1])
sys.exit(0)