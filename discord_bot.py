import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
# On récupère notre token discord dans l'env de Railway
bot_token = os.environ.get("MTE4NDQyNzM1NzI4NTY2NjkyNw.GI9F5V.ZkFplTlRzFDlzChTUOLf0-iiUs8YLj1vIdmjzI")

# Pour lancer le bot
client.run(MTE4NDQyNzM1NzI4NTY2NjkyNw.GI9F5V.ZkFplTlRzFDlzChTUOLf0-iiUs8YLj1vIdmjzI)
