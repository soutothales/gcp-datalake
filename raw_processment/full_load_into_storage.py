# This file will be responsible for loading data into storage service

import os
from google.cloud import storage

import sys as sys
sys.path.append( '..' )
import constants as constants

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../{}".format(constants.GCS_API_KEY_FILE)

storage_client = storage.Client()

chosen_bucket = storage_client.get_bucket(constants.GCS_BUCKET_NAME)

filename = constants.TEAMS_DATA_FILE

upload_file = os.path.join("../data/", filename)

blob = chosen_bucket.blob("raw/" + filename)

blob.upload_from_filename(upload_file)

