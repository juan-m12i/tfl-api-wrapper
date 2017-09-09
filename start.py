""" change name """

from tfl_api import TfLAPI
from cfg import config

import logging
import argparse
parser = argparse.ArgumentParser(description='This is a demo.')
parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level")

args = parser.parse_args()
if args.logLevel:
    level = args.logLevel
else:
    level = "INFO"


logging.basicConfig(
    filename="start-"+level+".log",
    level=getattr(logging, level),
    #format="%(asctime)s:%(levelname)5s:%(filename)s:%(funcName)20s:%(lineno)4s:%(message)s"
    format="%(asctime)s:%(levelname)5s:%(message)s"
    )

credentials = config.get_credentials()
TfL = TfLAPI(credentials["app_id"], credentials["app_key"])
arrivals = TfL.get_bus_arrivals("c2", "490003380N")
stopPoints = TfL.get_stop_points_by_location(51.5, -0.12)

