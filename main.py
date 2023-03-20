import discord
import os
import requests
import json
import random
from replit import db
from discord.ext import commands
from keep_alive import keep_alive
from discord import Message
from discord.client import Client

client = discord.Client()

'''
notes and ideas:
#winnie gives you coffee,, either just as a textbot or as a role/color select with buttons
#winnie talks like an active member,, either through validations (API?) or just randomly texting the chat once there's been little inactivity
#winnie has nsfw responses she can only respond to in the nsfw chat
'''

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "numb"]

starter_encouragements = [
  "You are never wrong for feeling a certain way, but it hurts me to see you so hurt! :cry:",
  "Please hang in there, even if it is only so we can keep chatting! :sunflower:",
  "You are an amazing person, and you're going to create beautiful things! :white_flower:",
  "Even though the world will try to keep you down, I will always be here for you :two_hearts:",
  "I only wish I could scoop you up and take you away to a kinder place! :pleading_face:",
  "No one should ever have to be as strong as you've been, but I admire your bravery nonetheless! :wilted_rose:"
]
mean_words = ['hate you', 'hate u', 'suck my dick', 'fuk u', 'fuck you', 'fuck u', 'die', 'stfu', 'shut up', 'bitch', 'cunt', 'kill urself', 'kill yourself', 'jump off', 'whore', 'suck', 'twat', 'cocksucker', 'cock', 'bad', 'dick', 'fag','faggot', 'fucking', 'stupid']

starter_retorts = [
  "ok.", "Is that what your mom did?", "That was rude.", ":rofl: :rofl:", "I'm so sorry you're having a bad day", "Thanks :upside_down:", "En garde! :crossed_swords:", "Is this how you treat all your friends or am I just special?", "That almost hurt my feelings."]

#kickable_words = ["get api of bad words]

#get inspirational quotes through API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#get cat picture
def get_catpic():
  response = requests.get("https://api.thecatapi.com/v1/images/search")
  json_data = json.loads(response.text)
  pic = json_data[0]['url']
  return(pic)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

#call a quote through msg
  if msg.startswith('inspire me'):
    quote = get_quote()
    await message.channel.send(quote)

#call a cat pic
  if msg.startswith('meow'):
    pic = get_catpic()
    await message.channel.send(pic)

#call encouragement using sad_words in msg 
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

#call retort using mean_words in msg 
  if any(word in msg for word in mean_words) and ('winnie' or 'Winnie' in msg):
    await message.channel.send(random.choice(starter_retorts))

#ban peoople who say kickable words
  for word in kickable_words:
    if word in msg:
      await message.author.kick()  # get the author of the message and kick them.
        
'''
#roles with buttons
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name ='adult')
    await client.add_roles(member,role)
    print(f'{member} was given {role}')

import discord.utils 
@client.event
async def role(ctx, * role: discord.Role):
  user = ctx.message.author
  await user.add_roles(role)
'''
keep_alive()
client.run(os.getenv('TOKEN'))