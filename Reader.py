import json as json
from configuration import configuration
import os as os

def config_getter()->configuration:
    file = open(os.getcwd()+'\\JSON_storage'+'\\config.json', "r")
    json_data = json.loads(file.read())
    file.close()
    return configuration.from_json(json_data["conf"]) 




