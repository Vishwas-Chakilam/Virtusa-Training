try:
    with open('log.txt', 'a') as f:
        f.write('Log entry added.\n')
    with open('log.txt', 'r') as f:
        print(f.read())
except IOError as e:
    print(f'File operation failed: {e}')