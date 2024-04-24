from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Database variables
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_NAME = getenv("DB_NAME")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")

# Telegram variables
BOT_TOKEN = getenv("BOT_TOKEN")


# Tomorrow.io variables (weather service)
WEATHER_API_KEY = getenv("WEATHER_API_KEY")
WEATHER_URL = getenv("WEATHER_URL")