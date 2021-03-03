import os, shutil

path = input("Enter Name of the Directory to be sorted: ")
list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext=="":
        continue
    if os.path.exists(path + "/" + ext):
        shutil.nove(path + "/" + file, path + '/' + ext + "/" + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + "/" + file, path + '/' + ext + "/" + file)
