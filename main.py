import discord
import os
import pandas as pd
from keep_alive import keep_alive
import random
from os import system
import time
import threading
import datetime

# Resetting, acutally pointless
# def reset():
#   while True:
#     time.sleep(180)
#     print("Rebooting...")
#     system("busybox reboot")
# t1 = threading.Thread(target = reset)
# t1.start()

# Declaration and reading of the main dictionary file
dic = None
spreadsheet_id = "YOUR_SPREADSHEET_ID"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv")
df.drop('Wstęp', inplace=True, axis=1)
dic = df

# Refreshing dictionary
def downloadSheet():
  while True:
    global dic
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv")
    df.drop('Wstęp', inplace=True, axis=1)
    dic = df
    now = datetime.datetime.now()
    print(f"Dictionary downloaded, newest version is from {now.day}.{now.month} {now.hour}:{now.minute}:{now.second}")
    time.sleep(300)

# Starting the refreshing thread
t2 = threading.Thread(target = downloadSheet)
t2.start()

# Preparing

keep_alive()
client = discord.Client()
STOP_FLAG = False

# Functions
def falseFlag():
  global STOP_FLAG
  STOP_FLAG = False

def trueFlag():
  global STOP_FLAG
  STOP_FLAG = True

# Purely esthetical thing
def gradient(colors):
  arr = colors
  for i in range(len(arr)):
    arr[i] = int(arr[i],16) - 3
    if arr[i] < 0:
      arr[i] = 0
    arr[i] = str(hex(arr[i]))[2:]
    if (len(arr[i])<2):
      arr[i] = "0" + arr[i]
  return arr

def makeColor(colors):
  c = ""
  for i in colors:
    c = c.join(i)
  return c


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    # STOPPING
    if message.content.startswith('?kon'):
        trueFlag()

    # The main function - searches for phrase in the whole line
    if message.content.startswith('?jak'):
        word = (message.content).lower()
        try:
          word = word.split()
          word = (word[1:])
          phrase = ""
          phrase = ' '.join([str(elem) for elem in word])
        except:
          return
        await message.channel.send("Szukanie wpisu: \""+phrase+"\"")
        found = False
        results = []
        for i in range(len(dic["A"])):
          try:
            if("[" in dic["A"][i].lower()):
                temp = dic["A"][i]
                temp = temp.split('[')
                temp = temp[1:]
                temp = ' '.join([str(elem) for elem in temp])
                temp = temp.lower()
                if(phrase in temp):
                  found = True
                  
                  if (isinstance(dic["Przypisy"][i],str)):
                    results.append([dic["A"][i],dic["Przypisy"][i]])
                  else:
                    results.append([dic["A"][i],"\u200b"])
            else:
              if(phrase in dic["A"][i].lower()):
                found = True
                if (isinstance(dic["Przypisy"][i],str)):
                    results.append([dic["A"][i],dic["Przypisy"][i]])
                else:
                    results.append([dic["A"][i],"\u200b"])
          except AttributeError:
            pass
        

        if found:
          falseFlag()
          await message.channel.send("Znaleziono następujące wyniki:")
          colors = ["%02x" % random.randint(0, 0xFF),"%02x" % random.randint(0, 0xFF),"%02x" % random.randint(0, 0xFF)]
          colors = gradient(colors)
          c = makeColor(colors)
          color = "%06x" % random.randint(0, 0xFFFFFF)
          embed=discord.Embed(color = int(c,16))
          for n in range(len(results)):
            if(STOP_FLAG):
              break
            embed.add_field(name=results[n][0], value=results[n][1], inline=False)
            if(not (n + 1)  % 20):
              await message.channel.send(embed=embed)
              colors = gradient(colors)
              c = makeColor(colors)
              embed=discord.Embed(color = int(c,16))
        else:
          await message.channel.send("Niestety, nic nie znaleziono.")

        # If there are any left to show
        try:
            await message.channel.send(embed=embed) 
        except:
            pass
        await message.channel.send("Koniec wyszukiwania!")

        falseFlag()

    # Zob - searches for exact lędzki phrase
    if message.content.startswith('?zob'):
        word = (message.content).lower()
        try:
          word = word.split()
          word = (word[1:])
          phrase = ""
          phrase = ' '.join([str(elem) for elem in word])
        except:
          return
      
        await message.channel.send("Szukanie wpisu: \""+phrase+"\"")
        found = False
        results = []
        for i in range(len(dic["A"])):
          try:
            if("[" in dic["A"][i].lower()):
                temp = dic["A"][i]
                temp = temp.split('[')
                temp = temp[:1]
                temp = ' '.join([str(elem) for elem in temp])
                temp = temp.lower()
                if(phrase.strip() == temp.strip()):
                  found = True
                  
                  if (isinstance(dic["Przypisy"][i],str)):
                    results.append([dic["A"][i],dic["Przypisy"][i]])
                  else:
                    results.append([dic["A"][i],"\u200b"])
            else:
              if(phrase == dic["A"][i].lower()):
                found = True
                if (isinstance(dic["Przypisy"][i],str)):
                    results.append([dic["A"][i],dic["Przypisy"][i]])
                else:
                    results.append([dic["A"][i],"\u200b"])
          except AttributeError:
            pass

        if found:
          falseFlag()
          await message.channel.send("Znaleziono następujące wyniki:")
          colors = ["%02x" % random.randint(0, 0xFF),"%02x" % random.randint(0, 0xFF),"%02x" % random.randint(0, 0xFF)]
          colors = gradient(colors)
          c = makeColor(colors)
          color = "%06x" % random.randint(0, 0xFFFFFF)
          embed=discord.Embed(color = int(c,16))
          for n in range(len(results)):
            if(STOP_FLAG):
              break
            embed.add_field(name=results[n][0], value=results[n][1], inline=False)
            if(not (n + 1)  % 20):
              await message.channel.send(embed=embed)
              colors = gradient(colors)
              c = makeColor(colors)
              embed=discord.Embed(color = int(c,16))
        else:
          await message.channel.send("Niestety, nic nie znaleziono.")

        # If there are any left to show
        try:
            await message.channel.send(embed=embed) 
        except:
            pass
        await message.channel.send("Koniec wyszukiwania!")

        falseFlag()

# Gets user token from secret variables
client.run(os.getenv('TOKEN'))

