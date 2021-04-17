import logging
from decouple import config
import discord

TOKEN = config("TOKEN")
WELCOME_GUILD = config("WELCOME_GUILD")
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_member_join(member):
    print(member)
    guild = member.guild
    to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
    print(to_send)
    await guild.system_channel.send(to_send)


client.run(TOKEN)