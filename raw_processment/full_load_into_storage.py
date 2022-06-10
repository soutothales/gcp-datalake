# This file will be responsible for loading data into storage service

import os
from google.cloud import storage

import sys as sys
sys.path.append( '..' )
import constants as constants

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../{}".format(constants.GCS_API_KEY_FILE)

bucket_name = constants.GCS_BUCKET_NAME
filename = constants.TEAMS_DATA_FILE

def upload_file(bucket_name, file_name):
    try:
        storage_client = storage.Client()
        chosen_bucket = storage_client.get_bucket(bucket_name)
        upload_file = os.path.join("../data/", file_name)
        blob = chosen_bucket.blob("raw/" + file_name)
        blob.upload_from_filename(upload_file)

        return True
    except Exception as e:
        print(e)
        return False

upload_file(bucket_name, filename)
