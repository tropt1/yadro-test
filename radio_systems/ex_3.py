import sys

if len(sys.argv) != 3:
    print("Usage: python ex_3.py <file> <word>")
    sys.exit(1)

file_path, search_word = sys.argv[1], sys.argv[2]

with open(file_path, 'r') as f:
    for line in f:
        if search_word.lower() in line.lower():
            print(line.strip())

