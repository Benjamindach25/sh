# ©️ DKBOTZ or https://t.me/DKBOTZ
# Coded By https://t.me/DKBOTZHELP 
# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", '25066000')) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", 'e6d75cc0240eee86135cb962b0ecea50') #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", '6685005337:AAG7OtmVYKz8Jr0PL63cL_ikuaOqNo2eadg') # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", 'cluster')
DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://Cluster0:AMRKS@cluster0.6sxfz9f.mongodb.net/?retryWrites=true&w=majority') # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", '1006159057')) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1744829025)
#  Optionnal variables
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", '-1002117005762') # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "ANLINKS_IN") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "True" 


# SHORTNER
SHORT_METHOD = 1 # 2 method added 1 and 2
SHORTNER_LINK = os.environ.get("SHORTNER_LINK", 'Anlinks.in')
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", 'https://t.me/ANLINKS_IN')
SIMPLE_MODE = os.environ.get("SIMPLE_MODE", False)
