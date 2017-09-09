import json

def get_credentials():
    with open('config.cfg') as data_file:    
        data = json.load(data_file)
    return data["credentials"]

