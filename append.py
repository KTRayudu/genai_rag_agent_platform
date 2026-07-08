import sys

def append_to_file(filepath, content):
    with open(filepath, 'a') as f:
        f.write(content)

if __name__ == "__main__":
    filepath = sys.argv[1]
    content = sys.stdin.read()
    append_to_file(filepath, content)
