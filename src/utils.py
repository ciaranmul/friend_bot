import sys
import os
import random
import json

from os.path import join, dirname
from dotenv import load_dotenv

def get_random_quote():
    """ Returns random quote from quotes file"""

    with open(get_env("DATA_FILE", __file__), 'r') as quotes_file:
        quotes = json.load(quotes_file)
    
    return random.choice(quotes)


def get_env(env_key, filepath):
    """ Get environment variables """
    
    # Create .env file path
    dotenv_path = join(dirname(filepath), '.env')
    # Load file from the path
    load_dotenv(dotenv_path)
    
    # Accessing variables
    try: 
        return os.getenv(env_key)
    except Exception as e:
        return e