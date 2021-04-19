import logging
from decouple import config
import discord
from profiles.quora import User
TOKEN = config("TOKEN")
UNVERIFIED_ROLE_ID = int(config("UNVERIFIED_ROLE_ID"))
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(message)s",
    level=logging.INFO,
)

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
    welcome_text = """Hey {}, welcome to {}! 

Please head over to the <#776135350287728690> and introduce yourself. Making an introduction is mandatory, to gain access to the server.
Read the <#776147848709275679> channel and abide by it, please.
For main announcements, we have <#776331788062687242> channel. You can take up self roles in <#776791052924616745> channel (after verification).

Hope you enjoy your stay here :slight_smile:""".format(member.mention, guild.name)
    await guild.system_channel.send(welcome_text)
    role = guild.get_role(UNVERIFIED_ROLE_ID)
    await member.add_roles(role)

async def get_quora(username):
    user = User(username)
  #  if user.firstName is not None and user.lastName is not None:
        #embed = discord.Embed(title=)
  #  else:
    #    embed = discord.Embed

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!quora'):
        username = message.content[7:]
        await message.channel.send(User(username))


client.run(TOKEN)
