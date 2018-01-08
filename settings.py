import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LINE_USER_ID = os.environ.get("LINE_USER_ID")
FEEDER_WS_URL = os.environ.get("FEEDER_WS_URL")
FEEDER_URL = os.environ.get("FEEDER_URL")
