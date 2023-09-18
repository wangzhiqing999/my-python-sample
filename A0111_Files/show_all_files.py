import sys
import os

"""
显示指定目录下的所有文件名，以及文件的大小.
"""


def show_path_fileinfo(path):
    with os.scandir(path) as entries:
        for entry in entries:            
            if (entry.is_dir()):
                show_path_fileinfo(entry)
            else:                
                file_size = entry.stat().st_size   # os.path.getsize(entry.path)
                print(entry.path, file_size)
                



def show_all_files():

    if (len(sys.argv) == 1):
        print("需要指定目录！")
    else:
        show_path_fileinfo(sys.argv[1])








show_all_files()