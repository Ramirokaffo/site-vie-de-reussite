
from django.core.files.storage import default_storage
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_images_url(path):
    filenames = [f for f in os.listdir(path)]
    list_files = []
    for element in filenames:
        myfile: str = os.path.join(path, element)
        if os.path.isfile(myfile):
            list_files.append({"title": element.split(".")[0], "value": os.path.join("/media", myfile.split("/media/")[-1])})
        else:
            list_files += get_images_url(myfile)
    return list_files


def delete_migrations_files():
    # print(BASE_DIR)
    filenames = [f for f in os.listdir(BASE_DIR) if not os.path.isfile(f)]
    # print(filenames)
    migrations_folders = []
    for folder in filenames:
        mirations_path = os.path.join(folder, "migrations")
        if os.path.isdir(mirations_path):
            migrations_folders.append(mirations_path)
    print(migrations_folders)
    migrations_files = []
    for dir in migrations_folders:
        lis_dir = os.listdir(dir)
        migrations_files += [os.path.join(dir, f) for f in lis_dir if f.endswith(".py") and f != "__init__.py"]
    
    print(migrations_files)
    
    for file in migrations_files:
        os.remove(file)
    # list_files = []
    # for element in filenames:
    #     myfile: str = os.path.join(path, element)
    #     if os.path.isfile(myfile):
    #         list_files.append({"title": element.split(".")[0], "value": os.path.join("/media", myfile.split("/media/")[-1])})
    #     else:
    #         list_files += get_images_url(myfile)
    # return list_files

delete_migrations_files()
