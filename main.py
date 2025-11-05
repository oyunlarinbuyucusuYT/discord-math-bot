import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import re

load_dotenv(override=True)
TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "merhaba":
        await message.channel.send("merhaba")


    elif message.content.lower().startswith("!hesapla"):

        expression = message.content[len("!hesapla "):].strip()

        try:
            result = eval(expression)
            await message.channel.send(f"Sonuç: {result}")
        except Exception as e:
            await message.channel.send("Geçersiz ifade! Lütfen doğru bir matematiksel işlem girin.")
    
    await bot.process_commands(message)

bot.run(TOKEN)