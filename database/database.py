import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

db = psycopg.connect(os.getenv('DATABASE_URI', ''))


