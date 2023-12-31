import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", discord.py])

import discord
from discord.ext import commands

# Your bot token
TOKEN = zLOtNpClKWSYFxs0ZeuLkY8EeVX_mV86

# Server IDs (replace these with your server IDs)
server1_id = 1102112870583521364
server2_id = 1071613385910792262

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Share ban
@bot.command()
async def share_ban(ctx, user_id: int, reason: str):
    # Get the member object for the given user ID
    member = bot.get_user(user_id)

    if not member:
        await ctx.send("User not found.")
        return

    # Share the ban to both servers
    server1 = bot.get_guild(server1_id)
    server2 = bot.get_guild(server2_id)

    if server1 and server2:
        # Ban the user on both servers
        await server1.ban(member, reason=reason)
        await server2.ban(member, reason=reason)
        await ctx.send(f"{member.mention} has been banned on both servers for: {reason}")
    else:
        await ctx.send("Could not find both servers.")

# Run the bot
bot.run(TOKEN)
