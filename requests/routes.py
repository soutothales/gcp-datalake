# This file will include the routes that will be called by the API

# Import section
import requests as requests
import json as json

import sys as sys
sys.path.append( '..' )
import constants as constants


auth_header = {"X-Auth-Token": constants.TOKEN_API}
response = requests.get(constants.TEAMS_URL, headers=auth_header)
response_json = response.json()

with open(constants.TEAMS_DATA_JSON_PATH, "w") as outfile:
    json.dump(response_json, outfile)