from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgC5N5tHMOhlW5-gTYM1vtOYFBt3Wq794eacFqVtU1KmYyEsSiDw12oN3W1cwnKisYivfWYxW2UichNoX6FoTZ53n6jbG93nZw9bTZvSc8sTUWE-0NZ5xRH3cK6KAkpJw0YlQrQ7QC1RvoBcCO77x4tnKcKwfBHsGKMQv4neF1PU9GvOEmFZL7Mqm3G22Kik00_VXEQje0KzS__nhvl4B1blZ69HY6R-7uelU6Ky9YtH02KKa7SSIFkoafHdq7wT527zdYavF0gcXOkM8Z8cDJBaAu0lrbOJfPjBNx47QvVL1_TmLkUCeujK2behI2tLWY0hoAWQxRgEWHgVJDXGODtcdmKkBAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5635983147:AAHhrmR9gMjabmMEw6c2OVDPZindBhj5F-o")
BOT_NAME = getenv("BOT_NAME", "SeCReT MuSiC") 
API_ID = int(getenv("API_ID", "18482353"))
API_HASH = getenv("API_HASH", "9f7840b7015b359a49e142ce42decd71")
BOT_USERNAME = getenv("BOT_USERNAME", "secretmusicrobot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SECRETMAN5/can")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "55"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5531642054").split()))
