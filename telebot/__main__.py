from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram import filters
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path("./telebot/src/configs/.env"))

bot: Client = Client(
    name=os.environ.get("APP_NAME"),
    api_hash=os.environ.get("API_HASH"),
    api_id=os.environ.get("API_ID"),
    bot_token=os.environ.get("BOT_TOKEN")
)

@bot.on_message(filters.command("start"), filters.private)
async def start(client: Client, message: Message):
    
    await message.reply(f"Hello {message.from_user.mention}")
    
@bot.on_message(filters.command("wakeup"), filters.private)
async def wakeup(client: Client, message: Message):
    
    await client.send_message(chat_id=os.environ.get("ADMIN"), text=".alive")

@bot.on_message(filters.command("scrape"), filters.private)
async def scrape(client: Client, message: Message):
    
    if len(message.text.split(" ")) == 1 or len(message.text.split(" ")) >= 3:
        await client.send_message(chat_id=message.chat.id, text="No ha introducido ningun hashtag valido, introduzca uno") 
    else:
        await client.send_message(chat_id=os.environ.get("ADMIN"), text=f".search {message.text.split(" ")[1]} {message.chat.username}")      

if __name__ == "__main__":
    print("starting bot")
    bot.start()
    print("bot started")
    bot.loop.run_forever()