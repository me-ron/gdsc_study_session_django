import os
import datetime
import shutil

folder_name = "last_24hours"
current_directory = os.getcwd()
now = datetime.datetime.now()
files = os.listdir(current_directory)

# check if the folder exists in the current directory
if not os.path.exists(folder_name):
    # create the folder
    os.makedirs(folder_name)
new_directory = os.path.join(folder_name)


def list_all():

    files = os.listdir(current_directory)

    for file in files:
        print(file)

def identify(filename):
    modified_time = os.path.getmtime(filename)
    modified_time = datetime.datetime.fromtimestamp(modified_time)

    created_time = os.path.getctime(filename)
    created_time = datetime.datetime.fromtimestamp(created_time)

    difference_modified = now - modified_time
    difference_created = now - created_time

    if difference_modified < datetime.timedelta(hours=24) or difference_created < datetime.timedelta(hours=24):
        return True
    return False

def move(filename):
    shutil.move(filename, new_directory)

def update_files():
    for file in files:

        if identify(file):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file, 'a') as f:
                f.write("\n" + timestamp)
                move(file)
            