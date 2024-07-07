import os
import json
from configuration import configuration

def config_setter(conf:configuration):
    file_path = os.getcwd()+'\\JSON_storage'+'\\config.json'
    with open(file_path, 'w', encoding='utf-8') as config_file:
        json.dump({"conf":conf.to_json()}, config_file)
        config_file.close()
    print('Configuration file updated successfully')

