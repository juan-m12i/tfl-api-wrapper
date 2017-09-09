import json
import os
import logging


def get_credentials(filepath = None):

    if filepath is None:
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "config.cfg"
        filepath = os.path.join(script_dir, rel_path)
        logging.debug(filepath)

    with open(filepath) as data_file:    
        data = json.load(data_file)
    return data["credentials"]

