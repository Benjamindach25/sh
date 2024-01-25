from pyrogram.types import *
from config import *



SIMPLE_START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Update Channel", url="https://t.me/ANLINKS_IN"),
        InlineKeyboardButton("Support 🤝", url="https://t.me/Anlinks_in_support")
        ],[
        InlineKeyboardButton("Connect To Anlinks🛠️", url=f"https://Anlinks.in/member/tools/api")
    ]
])



BALANCE_TEXT = '''Your Details

Username - {username}

Publisher Balance - {pbalance}

Referral Balance - {rbalance}

Total Balance - {tbalance}

'''

ACCOUNT_TEXT = '''Your Details

Username - {username}

Publisher Balance - {pbalance}

Referral Balance - {rbalance}

Total Balance - {tbalance}

'''

START_MESSAGE = '''**Hello, {user}
I Am {site} , Bulk Link Converter. I Can Convert Links Directly From Your {site} Account,
    
1. Go To 👉 https://{site}/member/tools/api 

2. Than Copy API Key

3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)

(See Example.👇)
Example: /api cbd63775f798fe0e58c67a56e6ce8b70c495cda4 

 ⭐️ If you need any help or Support Contact Us at @AnLinks_in_support.
'''

HELP_MESSAGE = '''
**Hey! My name is {firstname}. I am a {username}.**

Features 

- [Hyperlink](https://t.me/{username})
- Buttons convert support
- Header and Footer Text support
- Replace Username
- Banner Image

Helpful commands:

- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!
If You Have Any Problem Then Contact - @DKBOTZHELP_2

Available commands:

- /api - Use This Cmd To Add API
- /header - Set Header Text
- /footer - Set Footer Text
- /username - Set Username
- /banner_image - Set A Banner For Post
- /me - Your Settings Details
- /balance - Get Your Balance Info
- /features - Get Features Info

Use the commands to know more about the same
Below are some features I provide'''


FEATURES_MESSAGE = '''
**Hey! My name is {firstname}. I am a {username}.

Available commands:

- /api - Use This Cmd To Add API
- /header - Set Header Text
- /footer - Set Footer Text
- /username - Set Username
- /banner_image - Set A Banner For Post
- /me - Your Settings Details
- /balance - Get Your Balance Info
- /features - Get Features Info**'''

ABOUT_TEXT = """
**My Details:**
`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)

`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)
"""


CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""




HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf'),
        #InlineKeyboardButton('Admins', callback_data=f'admins_list'),    Not Required Because Users Can See Admin Of Bot
    ],

    [
        
        InlineKeyboardButton('Home', callback_data='start_dkbotz')
        
    ],


])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_dkbotz'),
        InlineKeyboardButton('Help', callback_data=f'help_dkbotz')
    ],
    [
        InlineKeyboardButton('💵 Balance', callback_data='dkbotz_balance')
    ],
    [
        InlineKeyboardButton('❌ Close', callback_data='delete')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('⬅️ Back', callback_data=f'help_dkbotz')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://{base_site})

- {base_site} API: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/api [api]`
            
Ex: `/api cbd63775f798fe0e58c67a56e6ce8b70c495cda4`

Get API From [{base_site}](https://{base_site}/)

Current {base_site} API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \n
To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username` (without @)

This username will be automatically replaced with other usernames in the post

To remove this username, `/username remove`"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
