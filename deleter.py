import os
from pprint import pprint
import send2trash
from config import Config


cfg = Config()
direc_to_walk = cfg.tv_direc


def find_empty_folders():
    empty_folders = []
    for folder, subfolder, file in os.walk(direc_to_walk):
        if len(file) == 0 and len(subfolder) == 0:
            empty_folders.append(folder)
    print('the following empty folders were found:')
    pprint(empty_folders)
    return empty_folders


# this section then deletes the empty directories
def delete_empties(list_of_empty_folders):
    for folder in list_of_empty_folders:
        send2trash.send2trash(folder)


empties = find_empty_folders()
delete_empties(empties)
