import logging
from decouple import config
import discord
from profiles.quora import User
TOKEN = config("TOKEN")

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.all()
#intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_member_join(member):
    print(member)
    guild = member.guild
    introduction = client.get_channel(INTRO_CHANNEL)
    rules = client.get_channel(RULE_CHANNEL)
    announcements = client.get_channel(ANN_CHANNEL)
    self_roles = client.get_channel(ROLE_CHANNEL)
    
    to_send = """Hey {0.mention}, welcome to Quorans! 
Before moving forward please head over to the <#776135350287728690> channel and introduce yourself. Making an introduction is mandatory, to gain access to the server.
Read the <#776147848709275679> channel and abide by it, please.
For main announcements, we have <#776331788062687242> channel. You can take up self roles in <#776791052924616745> channel.
Enjoy your stay here, have fun slight_smile""".format(member)
    await guild.system_channel.send(to_send)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!quora'):
        username = message.content[7:]
        try:
            await message.channel.send(User(username))
        except Exception as e:
            await message.channel.send(e)
          
    
client.run(TOKEN)
