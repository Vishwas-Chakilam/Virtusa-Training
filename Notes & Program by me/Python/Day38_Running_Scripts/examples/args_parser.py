import sys

if __name__ == '__main__':
    args = sys.argv
    print(f"Total arguments passed: {len(args)}")
    for i, arg in enumerate(args):
        print(f"Arg {i}: {arg}")