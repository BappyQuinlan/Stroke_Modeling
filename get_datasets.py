from kaggle.api.kaggle_api_extended import KaggleApi
import os
from os import path


def check_kaggle_account():
    filename = 'kaggle.json'
    homedir = os.path.expanduser("~") + '/.kaggle/'
    if path.exists(homedir + filename) == True:
        return True
    else:
        return False


class get_dataset:

    def __init__(self, filename, location):
        self.filename = filename
        self.location = location

        if check_kaggle_account() == True:
            api = KaggleApi()
            api.authenticate()

            f = self.filename
            p = self.location

            dir = './'

            # Signature: dataset_download_file(dataset, file_name, path=None, force=False, quiet=True)
            if path.exists(filename):
                os.remove(filename)
                api.dataset_download_file(p, f)
            else:
                api.dataset_download_file(p, f)

        else:
            return None
