# local settings sits here
#  such as logging
import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = str(os.getenv("SECRET_KEY"))
