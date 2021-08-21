import discord

from utils import get_env, get_random_quote, get_keywords_dict

client = discord.Client()
keywords_dict = get_keywords_dict()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if await responded_to_keyword(message):
        return

    if await responded_to_mention(message):
        return

async def responded_to_keyword(message):
    for keyword in keywords_dict.keys():
        if keyword in message.content:
            await message.channel.send(keywords_dict[keyword])
            return 1
    return 0

async def responded_to_mention(message):
    if client.user.mentioned_in(message):
        await message.channel.send(get_random_quote())
        return 1
    return 0

client.run(get_env("API_KEY", __file__))
    