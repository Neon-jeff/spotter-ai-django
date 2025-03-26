# REUSEABLE CONFIGURATIONS FOR THE .ENV FILE

import os
from pathlib import Path 
import environ

BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
