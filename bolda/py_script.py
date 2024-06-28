
from django.core.files.storage import default_storage
import os

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


