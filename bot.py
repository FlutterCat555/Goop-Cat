import sys
import time
import random
import datetime
import json

import discord
from discord.ext import commands

BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("i have gained sentience")

@bot.command()
async def add(ctx, x, y):
    if (x.isnumeric() and y.isnumeric()):
        x = int(x)
        y = int(y)
        screwyou = random.randint(0,4)
        if(screwyou==0):
            await ctx.send("idk lol")
        else:
            result = (x) + (y)
            await ctx.send("yeahh uhhh the answer is")
            time.sleep(1)
            await ctx.send("-# okay " + str(x) + " is a number, so is "+ str(y)+ " and i gotta add 'em.")
            time.sleep(1)
            await ctx.send("-# "+ str(x) + " times 50 is NOT "+ str(random.randint(20, 98)) +", so "+ str(y)+ " must equal "+ str(y)+ " so "+ str(x)+ " + "+ str(y)+ " = "+ str(x)+str(y) +", wait no")
            print()
            time.sleep(1)
            await ctx.send("i think its " + str(result) + " idk tho")
    else:
        await ctx.send("bitch that is not a number")



@bot.command()
async def subtract(ctx, x, y):
    if (x.isnumeric() and y.isnumeric()):
        x = int(x)
        y = int(y)
        screwyou = random.randint(0,4)
        if(screwyou==0):
             await ctx.send("idk lol")
        else:
            result = (x) - (y)
            await ctx.send("yeahh uhhh the answer is")
            time.sleep(1)
            await ctx.send("-# okay " + str(x) + " is a number, so is "+ str(y)+ " and i gotta subtract 'em.")
            time.sleep(1)
            await ctx.send("-# "+ str(x) + " divided by 50 is NOT "+ str(random.randint(-6, 10)) +", so "+ str(y)+ " must equal "+ str(y)+ " so "+ str(x)+ " - "+ str(y)+ " = " + str(y) + " - " + str(x) + "i , wait no")
            print()
            time.sleep(1)
            await ctx.send("i think its " + str(result) + " idk tho")
    else:
        await ctx.send("bitch that is not a number")

# ASK

@bot.command()
async def ask(ctx, x):
    author = ctx.message.author
    if(x):
        randask = random.randint(0,12)
        if (randask >= 8 and random.randint(0,3) == 0):
            randask = 11
        match(randask):
            case(0):
                await ctx.send("Yes")
            case(1):
                await ctx.send("No")
            case(2):
                await ctx.send("Maybe")
            case(3):
                await ctx.send("UwU nyaa :3")
            case(4):                    
                await ctx.send("NOwO")
            case(5):
                await ctx.send("go ultrakill yourself")
            case(6):
                await ctx.send("absolute cinema")
            case(7):
                await ctx.send("that seems kinda gay")
            case(8):
                await ctx.send("no horny! bad!!")
            case(9):
                await ctx.send("i stole your balls")
            case(10):
                await ctx.send("are you sure")
            case(11):
                await ctx.send("imma be real, thats the dumbest question ive heard in a while. you need to be put down.")
                await author.timeout(datetime.timedelta(minutes=2),reason="you got shot for asking dumb questions")
    else:
        await ctx.send("u didnt ask me anything nerd")


# COMPATIBILE

@bot.command()
async def ship(ctx,a,b):
    if(a==b):
        await ctx.send("the compatibility of " + str(a) + " and " + str(b) + " is 10 because they're the same thing")
        await ctx.send("selfships galore")
    else:
        print("normal logic")
        randcompatible = random.randint(0,10)
        await ctx.send("the compatibility of " + str(a) + " and " + str(b) + " is " + str(randcompatible))
        match(randcompatible):
            case(0):
                await ctx.send("-# a match made in hell")
            case(1):
                await ctx.send("-# i mean i wanna ship it")
            case(2):
                await ctx.send("-# i mean i still ship it")
            case(3):
                await ctx.send("-# at least they're somewhat TOLERABLE together")
            case(4):
                await ctx.send("-# at least they're TOLERABLE together")
            case(5):
                await ctx.send("-# mutual ''whatever''")
            case(6):
                await ctx.send("-# good pals, ain't ya?")
            case(7):
                await ctx.send("-# better pals, ain't ya?")
            case(8):
                await ctx.send("-# bwest fwends :3")
            case(9):
                await ctx.send("-# oh, get a room already")
            case(10):
                await ctx.send("-# cutest couple forever :hearts:")
                print("normal")



# ROULETTE

@bot.command()
async def roulette(ctx):
    author = ctx.message.author
    gun = random.randint(0,5)
    if(gun==0):
        gun = random.randint(0,1000)
        if (gun >= 0):
            await author.timeout(datetime.timedelta(minutes=1), reason="you are lose")
            await ctx.send("you fucking shot yourself in the fucking head you fucking idiot")
        else:
            await ctx.send("congrats! you shot yourself with an 39 outerballistic unsentimiental missiles, that's gonna leave a mark!!")
            await author.timeout(datetime.timedelta(minutes=30), reason="gambling problems")
    else:
        await ctx.send("you survived :c")

# GUN

@bot.command()
async def shoot(ctx, member:discord.Member):
    author = ctx.message.author
    gun = random.randint(0,6)
    if (author == member):
        match(gun):
            case(0):
                await ctx.send("you fucking shot yourself in the fucking head.")
                await member.timeout(datetime.timedelta(minutes=1), reason="suicide")
            case(1):
                await ctx.send("gun jammed :3")
            case(2):
                await ctx.send("you forgor to load it.")
            case(3):
                await ctx.send("you think you fucking shot yourself in the fucking head. Luckily, this was a backwards gun, you shot the air.")
            case(4):
                await ctx.send("pro tip: consider NOT aiming it at your head, ")
                await author.timeout(datetime.timedelta(minutes=1),reason="suicide")
            case(5):
                await ctx.send("haha, FUCKING DIE!")
                await member.timeout(datetime.timedelta(minutes=1),reason="you got shot")
            case(6):
                await ctx.send("you tried to shoot yourself, but the gun explodes in your hand")
                await member.timeout(datetime.timedelta(minutes=5),reason="you got misfired")
    else:
        match(gun):
            case(0):
                await ctx.send("you fucking shot " + str(member) + " in the fucking head.")
                await member.timeout(datetime.timedelta(minutes=1), reason="you got shot")
            case(1):
                await ctx.send("gun jammed :3")
            case(2):
                await ctx.send("you forgor to load it.")
            case(3):
                await ctx.send("you think you fucking shot " + str(member)+ " in the fucking head. Unluckily, this was a backwards gun.")
                await author.timeout(datetime.timedelta(minutes=1),reason="you got shot")
            case(4):
                await ctx.send("pro tip: consider NOT aiming it at your head, " + str(author))
                await author.timeout(datetime.timedelta(minutes=1),reason="you got shot")
            case(5):
                await ctx.send("FUCKING DIE, " + str(member))
                await member.timeout(datetime.timedelta(minutes=1),reason="you got shot")
            case(6):
                await ctx.send("you tried to shoot" + str(member) + ", but the gun explodes in your hand as the bullet is fired, injuring both of you")
                await author.timeout(datetime.timedelta(minutes=2),reason="you got misfired")
                await member.timeout(datetime.timedelta(minutes=2),reason="you got misfired")

#example commands

#user recognition example script
@bot.command()
async def amithemimic(ctx):
    if(ctx.author.id == 1008494180521213982):
        await ctx.send("its the mimic !!1!!21 !! !")
    else:
        await ctx.send("you are NOT the mimic")

@bot.command()
async def killyourself(ctx):
    if (ctx.author.id == 1008494180521213982):
        match(random.randint(0,4)):
            case(0):
                await ctx.send("error 404: life not found")
            case(1):
                await ctx.send("ok i die now")
            case(2):
                await ctx.send("POW you are DED")
            case(3):
                await ctx.send("owie ow ouch ow that hurted :c")
            case(4):
                await ctx.send("oh fuck")
        await ctx.send("-# fucking dies")
        sys.exit()
