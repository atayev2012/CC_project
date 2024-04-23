from dotenv import load_dotenv
import os

load_dotenv()

# Database variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Telegram variables
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Tomorrow.io variables (weather service)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")