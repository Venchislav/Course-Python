def iter_file(file_path):
    with open(file_path) as f:
        for line in iter(f.readline, ""):
            print(line.rstrip())


if __name__ == '__main__':
    iter_file('colors.txt')
