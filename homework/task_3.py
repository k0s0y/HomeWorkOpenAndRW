import os

BASE_PATH = os.getcwd()
DIR_FILES = 'other_files'
NAME_OF_NEW_FILE = "join.txt"

full_path = os.path.join(BASE_PATH, DIR_FILES)
path_of_join = os.path.join(BASE_PATH, NAME_OF_NEW_FILE)


def make_list_of_file(files_dir):
    file_list = {}
    sorted_dict = {}
    list_of_file = os.listdir('other_files')
    for file in list_of_file:
        file_path = os.path.join(files_dir, file)
        with open(file_path, 'r') as doc:
            lines = doc.readlines()
            file_list[file] = len(lines)
    sorted_values = sorted(file_list.values())
    for i in sorted_values:
        for k in file_list.keys():
            if file_list[k] == i:
                sorted_dict[k] = file_list[k]
                break
    return sorted_dict


def join_files(files_dir):
    # создаем файл куда сохраняем остальные (в другой директории, что бы избежать рекурсии)
    list_of_file = make_list_of_file(files_dir)
    for file in list_of_file:
        file_path = os.path.join(files_dir, file)
        with open(file_path, 'r') as doc:
            lines = doc.readlines()
            for line in lines:
                with open(path_of_join, 'a') as new_file:
                    new_file.write(line)


join_files(full_path)