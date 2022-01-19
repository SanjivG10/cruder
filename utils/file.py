import os

def file_exists(filename):
    return os.path.exists(filename)


def create_folder(folder_name):
    if not file_exists(folder_name):
        os.mkdir(folder_name)
    else:
        raise Exception(f"Folder name `{folder_name}` exists. Can you please delete it or rename output folder name?")



