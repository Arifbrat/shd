from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "5548856893:AAGaplJtK3C8y3A0x3l9ST9fQkiNr3rJNaU")
BOT_NAME = getenv("BOT_NAME", "SeCReT MuSiC") 
API_ID = int(getenv("API_ID", "18482353"))
API_HASH = getenv("API_HASH", "9f7840b7015b359a49e142ce42decd71")
BOT_USERNAME = getenv("BOT_USERNAME", "secretmusicrobot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SECRETMAN5/can")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "55"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5531642054").split()))
