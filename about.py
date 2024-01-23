from pyrogram import Client, filters


app = Client("my_bot")

@app.on_message(filters.command("about"))
   def about(client, message):
       if message.from_user.id == OWNER_ID:
           text = ABOUT_TEXT.format(OWNER_NAME)
           message.reply_text(text)
         app.run()
