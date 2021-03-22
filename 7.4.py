import os

file_size_list = []
tree_dirs = os.walk('venv')
adding_list = [file_size_list.append(os.stat(os.path.join(root, file)).st_size) for root, dirs, files in tree_dirs
               for file in files]
my_dict = {}
part_size_list = []
max_size = 10
min_size = 0
while min_size < max(file_size_list):
    tree_dirs = os.walk('venv')
    adding_list = [part_size_list.append(file) for root, dirs, files in tree_dirs for file in files
                   if min_size < os.stat(os.path.join(root, file)).st_size < max_size]
    my_dict[max_size] = len(part_size_list)
    part_size_list.clear()
    min_size = max_size
    max_size *= 10
print(my_dict)
