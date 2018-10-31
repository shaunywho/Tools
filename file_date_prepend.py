import os
from shutil import copyfile
from datetime import datetime
from dateutil import parser


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
    new_filepath = os.path.join(root,mod_time+file)

    os.rename(filepath,new_filepath)

def rename_files_in_folder(folderpath):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            if not file.startswith("."):
                if not check_if_dated(file):
                    add_date(root,file)


            




folderpath="/Users/shaun/Documents/Python/test_folder"
test=False


if __name__=="__main__":
    if test:
        for filename in range(10):
            with open(os.path.join(folderpath,str(filename)+".txt"), "w") as f:
                f.write("test")
    else:
        rename_files_in_folder(folderpath)
    
    