import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
MODEL_PATH = os.getenv("MODEL_PATH")
