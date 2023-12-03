#use pip install discord.py==1.4.2
import discord
from discord.ext import commands
import asyncio 


token = input("\033[0;96m[~\033[0;96m] \033[0;96mTOKEN - ")
prefix = input("\033[0;96m[~\033[0;96m] \033[0;96mPREFIX - ")
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
bot.remove_command('help')


@bot.command(description = "clones a server")
async def cloneserver(ctx): 
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
