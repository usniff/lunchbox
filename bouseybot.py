import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

TOKEN = 'NzE4NzA3NDc1Mjg4OTQ4Nzk3.Xt6vGA.5y60AYAHxwDSpBYMplaT7aeGFV8'


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await client.change_presence(activity=discord.Game(name='FCEL'))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Beep boop {0.author.mention}'.format(message))

        if message.content.startswith('!simpcheck'):
            possible_response = ['you are a simp', 'it looks like you are a simp','signs point to simp', 'early readings strongly suggest simp']
            response = random.choice(possible_response)
            await message.channel.send('checking...')
            await asyncio.sleep(2)
            
        if message.content.startswith('!ginger'):
            await message.channel.send('fetching ginger...')
            await asyncio.sleep(2)
            await message.channel.send('ginger says meow')
            ginger =  ['ginger.jpg', 'chairginger.jpg', 'cup.jpg','gun.jpg','tie.jpg']
            picture = random.choice(ginger)
            await message.channel.send(file=discord.File(picture))

        if message.content.startswith('!chucho'):
            await message.channel.send('walking aimlessly...')
            await asyncio.sleep(2)
            await message.channel.send('package delivered')
            await message.channel.send(file=discord.File('chucho.jpg'))
            
        if message.content.startswith('!advice'):
            advice = [
            'blow up your account',
            'all in tesla, is the most optimal choice',
            'it seems the only option is all in',
            'deep OTM calls',
            'consult WSB',
            ]
            aresponse = random.choice(advice)
            await message.channel.send('predicting the future...')
            await asyncio.sleep(3)
            await message.channel.send(aresponse)
            
        if message.content.startswith('!jay'):
            jay = ['jay1.jpg','jay2.jpg','jay3.jpg']
            jresponse = random.choice(jay)
            
            if jresponse == 'jay3.jpg':
                await message.channel.send('squeezing you in...')
                await asyncio.sleep(2)
                await message.channel.send('you have 1 minute.')
                await message.channel.send(file=discord.File(jresponse))
            elif jresponse == 'jay2.jpg':
                await message.channel.send('sending love...')
                await asyncio.sleep(2)
                await message.channel.send(file=discord.File(jresponse))
                await message.channel.send('good boy!')
            else:
                await message.channel.send('looking for jay...')
                await asyncio.sleep(2)
                await message.channel.send(file=discord.File(jresponse))
                await message.channel.send('A BIRD!')

client = MyClient()
client.run(TOKEN)