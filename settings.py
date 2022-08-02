## importing the load_dotenv from the python-dotenv module
from dotenv import load_dotenv


## using existing module to specify location of the .env file
from pathlib import Path
import os

def dotenv_conect():
    load_dotenv()
    env_path = Path('.')/'dev.env'
    load_dotenv(dotenv_path=env_path)

# retrieving keys and adding them to the project
# from the .env file through their key names

def get_db():
    dotenv_conect()
    return os.getenv("DB")
    

def get_url():
    dotenv_conect()
    return os.getenv("URL")



