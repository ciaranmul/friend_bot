import discord

from utils import get_env, get_random_quote

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send(get_random_quote())
        return

client.run(get_env("API_KEY", __file__))
    