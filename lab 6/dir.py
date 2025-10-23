import os
import shutil
import string

path = "C:\Games\ArtMoney"


# 1.
def show_files_and_dirs(path):
    if not os.path.exists(path):
        print("базовый минимум")
        return

    folders = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("Folders:", folders)
    print("Files:", files)
    print("All contents:", os.listdir(path))


# ex
print("__" * 20, "\n")
show_files_and_dirs(path)
print("__" * 20, "\n")


# 2
def check_path(path):
    print(f"Exists? {os.path.exists(path)}")
    print(f"Readable? {os.access(path, os.R_OK)}")
    print(f"Writable? {os.access(path, os.W_OK)}")
    print(f"Executable? {os.access(path, os.X_OK)}")


# example
check_path(path)
print("__" * 20, "\n")


# 3
def check_file_info(path):
    if os.path.exists(path):
        print("This path exists!")
        print("Folder:", os.path.dirname(path))
        print("File:", os.path.basename(path))
    else:
        print("ай ай без повода обнимай")


# ex
check_file_info(path)
print("__" * 20, "\n")


# 4.
def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        print("file not found!")
        return 0


# ex
lines_count = count_lines("C:\Games\ArtMoney\example.txt")
print(f"Number of lines: {lines_count}")
print("__" * 20, "\n")


# 5
def save_list_to_file(file_path, items):
    with open(file_path, "w") as file:
        for item in items:
            file.write(item + "\n")
    print(f"List saved to {file_path}")


# example
save_list_to_file("C:\Games\ArtMoney\example.txt", ["1337", "67", "228"])
print("__" * 20, "\n")


# 6.
def create_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as file:
            file.write(f"This is file {letter}.txt\n")
    print("Files A-Z created")


# example
create_files()
print("__" * 20, "\n")


# 7
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File {source} copied to {destination}")
    except FileNotFoundError:
        print("Source file not found")


# eaxple
copy_file("C:\Games\ArtMoney\example.txt", "C:\Games\ArtMoney\example_copy.txt")
print("__" * 20, "\n")


# 8.
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File {file_path} deleted!")
        else:
            print("No permission to delete the file")
    else:
        print("File does not exist!")


# example
delete_file("C:\Games\ArtMoney\example_copy.txt")
print("__" * 20, "\n")
