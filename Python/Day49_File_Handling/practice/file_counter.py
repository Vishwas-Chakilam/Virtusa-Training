def count_file_stats(filename):
    lines = 0
    words = 0
    with open(filename, 'w') as f:
        f.write("Hello World\nTest string\nYay")
        
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            words += len(line.split())
            
    return lines, words

l, w = count_file_stats('sample.txt')
print(f"Lines: {l}, Words: {w}")