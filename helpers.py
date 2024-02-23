# ©️ DKBOTZ or https://t.me/DKBOTZ
# Coded By https://t.me/DKBOTZHELP 
# Don't Edit

# temp db for banned 
import asyncio
import logging
import traceback

import aiohttp

import database
from config import ADMINS, REQ_CHANNEL
from database.join_reqs import JoinReqs as db2

class temp(object): # TrojanZ Idea of Temping
    BOT_USERNAME = None
    CANCEL = False
    FIRST_NAME = None
    START_TIME = None
    BANNED_USERS = []

class AsyncIter:    
    def __init__(self, items):    
        self.items = items    

    async def __aiter__(self):    
        for item in self.items:    
            yield item  

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration as e:
            raise StopAsyncIteration from e

class Helpers:
    def __init__(self):
        self.username = temp.BOT_USERNAME

    @property
    async def user_method(self):
        user_method = await database.db.get_bot_method(self.username)
        return user_method or "None"

    @property
    async def get_admins(self):
        x=''
        async for i in AsyncIter(ADMINS):
            x+= f"~ `{i}`\n"
        return x

async def is_subscribed(bot):

    if not REQ_CHANNEL:
        logger.info("No AUTH_CHANNEL or REQ_CHANNEL found")
        return True
    #elif query.from_user.id in ADMINS:
        #return True

    if db2().isActive():
        user = await db2().get_user(query.from_user.id)
        if user:
            logger.info(f"User found: {query.from_user.first_name}")
            return True
        else:
            return False
    if not REQ_CHANNEL:
        logger.info("AUTH_CHANNEL not found")
        return True
    try:
        user = await bot.get_chat_member(REQ_CHANNEL, query.from_user.id)
    except UserNotParticipant:
        return False
    except Exception as e:
        logger.exception(e)
        return False
    else:
        if not (user.status == enums.ChatMemberStatus.BANNED):
            logger.info("User Is a Member")
            return True
        else:
            return False

