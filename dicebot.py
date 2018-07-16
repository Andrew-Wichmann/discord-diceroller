import discord
import asyncio
import random
import re

# Load account token from other file
token = open("token", "r").read().strip()


# Global Initializations
client = discord.Client()
check_regex = re.compile("roll a (\d{1,3}) die(.*)", re.IGNORECASE)
# Note that any roll with more than 300ish dice is going to fail to send anyway
save_regex = re.compile("^[ns](\d{1,3})(.*)", re.IGNORECASE)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


@client.event
async def on_message(message):
    print("{}:{}{}:{}".format(
        message.author,
        message.server.name+":" if message.server else "",
        message.channel,
        message.content,
    ))
    # Roll a check (success on 3-6)
    if check_regex.match(message.content):
        m  = check_regex.match(message.content)
        number = random.randint(1,int(m.group(1)))
        await client.send_message(
            message.channel,
            "You rolled a {}".format(number)
        )

# Not currently used but I wanted AW to see a fun thing.
async def slow_talk(message, response):
    msg = await client.send_message(message.channel, "hmmmmmmmmm...")
    await asyncio.sleep(5)
    for i in range(len(response)+1):
        await client.edit_message(msg, response[:i])
        await asyncio.sleep(2)


# Actually kicks things off
client.run(token)
