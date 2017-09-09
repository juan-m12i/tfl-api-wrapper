""" change name """

from tfl_api import TfLAPI
from cfg import config
import logging

parser = argparse.ArgumentParser(description='This is a demo.')
parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level")


logging.basicConfig(filename="start-debug.log", level=logging.INFO)
logging.debug("start")
logging.basicConfig(filename="start-debug2.log", level=logging.WARNING)

credentials = config.get_credentials()

TfL = TfLAPI(credentials["app_id"], credentials["app_key"])
  
print (TfL.get_bus_arrivals("c2", "490003380N"))
  


args = parser.parse_args()
if args.logLevel:
    logging.basicConfig(level=getattr(logging, args.logLevel))