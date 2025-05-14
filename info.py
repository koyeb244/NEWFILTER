import re
from Script import script
from time import time

id_pattern = re.compile(r"^.\d+$")

def is_enabled(value, default):
    if isinstance(value, str):
        value = value.lower()
        if value in ["true", "yes", "1", "enable", "y"]:
            return True
        elif value in ["false", "no", "0", "disable", "n"]:
            return False
    return default

# Bot information
SESSION = "Media_search"
API_ID = 29483517
API_HASH = "e35a05d338376cbcd8162f810aed878d"
BOT_TOKEN = "7892042341:AAEGJE0qKT70cJvmniPQnObc1vpM23LX_B8"

# Bot settings
BOT_START_TIME = time()
CACHE_TIME = 300
USE_CAPTION_FILTER = False
PICS = [
    "https://envs.sh/YxC.jpg",
    "https://envs.sh/YxR.jpg",
    "https://envs.sh/YxH.jpg",
    "https://envs.sh/Yxk.jpg",
    "https://envs.sh/Yxv.jpg",
    "https://envs.sh/YxU.jpg",
    "https://envs.sh/Yx4.jpg"
]

# Admins, Channels & Users
ADMINS = [5756495153]
CHANNELS = [-1002334590710]
AUTH_USERS = ADMINS.copy()
AUTH_CHANNEL = -1002593166412
AUTH_GROUPS = -4755745005

# MongoDB information
DATABASE_URI = "mongodb+srv://user1:abhinai.2244@cluster0.7oaqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = "mn_files"

# Others
LOG_CHANNEL = -1002334590710
SUPPORT_CHAT = "mnbots_support"
P_TTI_SHOW_OFF = is_enabled("False", False)
IMDB = is_enabled("False", False)
SINGLE_BUTTON = is_enabled("True", True)
CUSTOM_FILE_CAPTION = script.CUSTOM_FILE_CAPTION
BATCH_FILE_CAPTION = "📂 <em>File Name</em>: <code>{file_name}</code>\n\n ♻ <em>File Size</em>:{file_size} </b>"
IMDB_TEMPLATE = "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝗋𝗌: {genres}"
LONG_IMDB_DESCRIPTION = is_enabled("False", False)
SPELL_CHECK_REPLY = is_enabled("True", True)
MAX_LIST_ELM = None
INDEX_REQ_CHANNEL = LOG_CHANNEL
FILE_STORE_CHANNEL = [-1002334590710]
MELCOW_NEW_USERS = is_enabled("True", True)
PROTECT_CONTENT = is_enabled("False", False)
PUBLIC_FILE_STORE = is_enabled("False", True)

# Log string
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += "IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n"
LOG_STR += "P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM directly.\n"
LOG_STR += "SINGLE_BUTTON is enabled, filename and file size will be shown in a single button.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled, filename and file size will be shown in separate buttons.\n"
LOG_STR += f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found, default captions will be used.\n"
LOG_STR += "Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, plot will be shorter.\n"
LOG_STR += "Spell Check Mode is enabled, bot will suggest related movies if movie not found.\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY mode is disabled.\n"
LOG_STR += f"MAX_LIST_ELM found, long list will be shortened to first {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "Full list of cast and crew will be shown in IMDB template; restrict by setting MAX_LIST_ELM.\n"
LOG_STR += f"Your current IMDB template is:\n{IMDB_TEMPLATE}"
