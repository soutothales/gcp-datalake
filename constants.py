# Util functions
import utils.utils as utils 


API_URL = "http://api.football-data.org/v4"

CURRENT_LEAGUE = "BSA"

TEAMS_URL = "{}/competitions/{}/teams".format(API_URL, CURRENT_LEAGUE)

TOKEN_API = utils.token_reader()

TEAMS_DATA_JSON_PATH = "../data/bsa_teams_data.json"