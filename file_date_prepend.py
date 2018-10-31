import os
from shutil import copy2
from datetime import datetime
from dateutil import parser
from collections import Counter
import pyperclip
import objc
import sys
import time
import unicodedata


def check_if_dated(file):
    date = file[0:8]
    try:
        datetime.strptime(date,"%Y%m%d")
        return True
    except ValueError:
        return False


def add_date(root, file):
    filepath = os.path.join(root,file)
    mod_time = os.path.getmtime(filepath)
    mod_time = datetime.fromtimestamp(mod_time)
    mod_time = mod_time.strftime("%Y%m%d")
    updated_files_directory = os.path.join(root,"updated_files")
    if not os.path.exists(updated_files_directory):
        os.makedirs(updated_files_directory)
    new_filepath = os.path.join(root,"updated_files",mod_time+file)
    copy2(filepath,new_filepath)
    print new_filepath+" created!"


def rename_files_in_folder(folderpath):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            if not file.startswith(".") and not check_if_dated(file):
                add_date(root,file)


            
def get_clipboard_filepaths():
    clipboard_paths = repr(pyperclip.paste())
    clipboard_paths = clipboard_paths.replace("u'","").replace("'","")
    clipboard_paths_list = clipboard_paths.split('\\n')
    basenames_list = [os.path.basename(clipboard_path) for clipboard_path in clipboard_paths_list]
    dirnames_list = [os.path.dirname(clipboard_path) for clipboard_path in clipboard_paths_list]
    return dirnames_list[0], basenames_list

def rename_files_from_clipboard():
    dirname, basenames_list = get_clipboard_filepaths()
    if len(basenames_list)==0:
        print 'Tool only works in a single directory and uses pathnames, use Alt Key after right clicking selection and choose "Copy "X" as pathname"'
    elif dirname=="":
        print 'Tool only works in a single directory and uses pathnames, use Alt Key after right clicking selection and choose "Copy "X" as pathname"'
    elif len(basenames_list)==1 and os.path.isdir(os.path.join(dirname,basenames_list[0])):
        folderpath = os.path.join(dirname,basenames_list[0])
        rename_files_in_folder(folderpath)
    else:
        rename_files_in_selection(dirname, basenames_list)


def rename_files_in_selection(root, files):
    for file in files:
        if not file.startswith(".") and not check_if_dated(file):
            add_date(root,file)
    




folderpath="/Users/shaun/Documents/Python/Tools/test_folder"
test=False


if __name__=="__main__":


    if test:
        for root, dirs, files in os.walk(folderpath):
            for file in files:
                os.unlink(os.path.join(root,file))
        for filename in range(10):
            with open(os.path.join(folderpath,str(filename)+".txt"), "w") as f:
                f.write("test")
    else:

        recent_value = pyperclip.paste()
        while True:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                rename_files_from_clipboard()
            time.sleep(0.1)
        
    