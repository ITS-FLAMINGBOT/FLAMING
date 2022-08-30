import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "5520909793"))
API_HASH = getenv("API_HASH", "3b5d73f27080334a1d730087b552519b")
BOT_TOKEN = getenv("BOT_TOKEN", "5546654031:AAH9mLaNOiTVfzesjSSlT7QqawqNdP4cRec")
STRING_SESSION = getenv("STRING_SESSION", "1BVtsOHEBu2e7ssbfeUIVXTojCMwXf0eHj4DT9Z9eb9cOK06aEhX8Qm4jVKzfuq5ggB0-k1JRK1LRN-AzWoCYEWL8ttPffUm4UAy8N_uGmCYJ6zqpzUpOiRAcvu4Rhs-1wiRq2Wv4K65CNcf3v0oc6WYwMluic_Hji7320dFCfozCm59IfFDeEkRDA-bW4Xr35jOOOvJMP2kt0A2vEf-lp4junByTmT6qm27XWuUMRrZQVhuBjWbD6iWsp51BWHOW7u1cHVxIPPuLlfV0_UpUN5Rmy0-ayxfOpdjcb4uy4rxnOkyARMN41lheMZ0LOPMVxJml8uTq0CLbNa5Zxblh0Nzymf8nrvU= ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5336023580").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-687989817"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5356564375").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITS-FLAMINGBOT/FLAMING")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "flaming")
