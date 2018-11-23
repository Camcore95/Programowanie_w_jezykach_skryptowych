import os


def print_files(path_to_file):
    print("Files in", path_to_file)
    for name in os.listdir(path_to_file):
        if os.path.isfile(os.path.join(path_to_file, name)):
            print(name)
        else:
            print_files(path_to_file + "/" + name)


path = input("Enter path: ")
print_files(path)
