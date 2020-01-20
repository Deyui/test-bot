import discord
import random
import asyncio
from discord.ext import commands
from discord import file
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!')

@client.command()
async def shutdown(ctx):
    await ctx.bot.logout()


@client.event
async def on_ready():
    print('{0.user} is ready.'.format(client))

@client.command()
async def roles(ctx):
    embed=discord.Embed(title="Roles", color=0x854e3a)
    embed.add_field(name='\u200b', value="Chino\nRize\nSyaro\nMegu\nRin\nMocha\nNatsume\nFuyu\nTakahiro\nAnko",inline=True)
    embed.add_field(name='\u200b', value="Cocoa\nChiya\nMaya\nAoyama\nYura\nEru\nChidori\nTippy\nWild Geese\nKigumin",)
    await ctx.send(embed=embed)


@client.command()
async def addrole(ctx, arg1, arg2=""):
    arg = arg1.capitalize()
    print(f'Arg: {arg} and Arg1: {arg1}')
    if arg2 != "":
        arg2 = arg2.capitalize()
        arg = arg + " " + arg2
    member = ctx.message.author
    print(f'Arg: {arg} and Arg1: {arg1}')
    rolename = discord.utils.get(member.guild.roles, name=arg)
    print(rolename)
    if rolename is None:
        await ctx.send('Role not found.')
        pass
    else:
        try:
            await member.add_roles(rolename)
            await ctx.send("Role added")
        except discord.Forbidden:
            await ctx.send('Role cannot be assigned.')
            pass
        except AttributeError:
            print('AttributeError')
            pass
        except TypeError:
            print('TypeError')
            pass


@client.command()
async def removerole(ctx, arg1, arg2=""):
    arg = arg1.capitalize()
    print(f'Arg: {arg} and Arg1: {arg1}')
    if arg2 != "":
        arg2 = arg2.capitalize()
        arg = arg + " " + arg2
    member = ctx.message.author
    rolename = discord.utils.get(member.guild.roles, name=arg)
    print(rolename)
    if rolename is None:
        print('Role is not found.')
        pass
    else:
        try:
            await member.remove_roles(rolename)
            await ctx.send("Role has been removed.")
        except discord.Forbidden:
            await ctx.send('Role cannot be assigned.')
            pass
        except AttributeError:
            print('AttributeError')
            pass
        except TypeError:
            print('TypeError')
            pass


yourchoice = ''
player = ""
please = ''
opponent = ""
result = ''
@client.command()
async def rps(ctx, choices, char=""):
    global yourchoice
    global player
    global please
    global opponent
    global result
    yourchoice = choices
    choices = choices.lower()

    if choices == 'rock' or choices == 'paper' or choices == 'scissors':
        pass
    else:
        return

    if char.lower() == "":
        a = 'chino'
        b = 'maya'
        c = 'megu'
        chimame = [a, b ,c]
        char = random.choice(chimame)

    if char.lower() == 'chino':
        d = 'C:\\Users\\duy0\\my-bot\\Python\\Chino\\scissors.gif'
        e = 'C:\\Users\\duy0\\my-bot\\Python\\Chino\\rock.gif'
        f = 'C:\\Users\\duy0\\my-bot\\Python\\Chino\\paper.gif'
        outcomes = [d, e, f]
        player = char
        please = random.choice(outcomes)
    elif char.lower() == 'maya':
        g = 'C:\\Users\\duy0\\my-bot\\Python\\Maya\\scissors.gif'
        h = 'C:\\Users\\duy0\\my-bot\\Python\\Maya\\rock.gif'
        i = 'C:\\Users\\duy0\\my-bot\\Python\\Maya\\paper.gif'
        outcomes = [g, h, i]
        player = char
        please = random.choice(outcomes)
    elif char.lower() == 'megu':
        j = 'C:\\Users\\duy0\\my-bot\\Python\\Megu\\scissors.gif'
        k = 'C:\\Users\\duy0\\my-bot\\Python\\Megu\\rock.gif'
        l = 'C:\\Users\\duy0\\my-bot\\Python\\Megu\\paper.gif'
        outcomes = [j, k, l]
        player = char
        please = random.choice(outcomes)
    else:
        await ctx.send("Character not found.")
        return
    print(please)
    print(player)
    print(choices)
    await ctx.send(file=discord.File(please))
    opponent = please.replace("C:\\Users\\duy0\\my-bot\\Python\\", "").replace("Megu", "").replace("Maya", "").replace("Chino", "").replace(".gif","").replace("\\","")
    print(yourchoice)
    print(opponent)
    result = ''
    if yourchoice.lower() == 'paper' and opponent == 'rock':
        result = 'Win'
    elif yourchoice.lower() == 'rock' and opponent == 'rock':
        result = 'Draw'
    elif yourchoice.lower() == 'scissors' and opponent == 'rock':
        result = 'Lose'
    elif yourchoice.lower() == 'rock' and opponent == 'paper':
        result = 'Lose'
    elif yourchoice.lower() == 'paper' and opponent == 'paper':
        result = 'Draw'
    elif yourchoice.lower() == 'scissors' and opponent == 'paper':
        result = 'Win'
    elif yourchoice.lower() == 'rock' and opponent == 'scissors':
        result = 'Win'
    elif yourchoice.lower() == 'paper' and opponent == 'scissors':
        result = 'Lose'
    elif yourchoice.lower() == 'scissors' and opponent == 'scissors':
        result = 'Draw'
    else:
        print('wtf')
    print(f'The result is: {result}')
    return result
    return choices
    return player
    return please
    return opponent

colors = ''
global r, g, b
@client.event
async def on_message(message):
    global result
    if result != '':
        colors = '122, 193, 240'
        print('Results have been detected!')
        try:
            if 'scissors' in message.attachments[0].filename and yourchoice.lower() == 'paper':
                print('Checking results...')
                result = 'Lost'
                opponent = 'scissors'
            if 'paper' in message.attachments[0].filename and yourchoice.lower() == 'paper':
                print('Checking results...')
                result = 'Draw'
                opponent = 'paper'
            if 'rock' in message.attachments[0].filename and yourchoice.lower() == 'paper':
                print('Checking results...')
                result = 'Won'
                opponent = 'rock'

            if 'scissors' in message.attachments[0].filename and yourchoice.lower() == 'rock':
                print('Checking results...')
                result = 'Won'
                opponent = 'scissors'
            if 'paper' in message.attachments[0].filename and yourchoice.lower() == 'rock':
                print('Checking results...')
                result = 'Lost'
                opponent = 'paper'
            if 'rock' in message.attachments[0].filename and yourchoice.lower() == 'rock':
                print('Checking results...')
                result = 'Draw'
                opponent = 'rock'

            if 'scissors' in message.attachments[0].filename and yourchoice.lower() == 'scissors':
                print('Checking results...')
                result = 'Draw'
                opponent = 'scissors'
            if 'paper' in message.attachments[0].filename and yourchoice.lower() == 'scissors':
                print('Checking results...')
                result = 'Won'
                opponent = 'paper'
            if 'rock' in message.attachments[0].filename and yourchoice.lower() == 'scissors':
                print('Checking results...')
                result = 'Lost'
                opponent = 'rock'

            if result == 'Won':
                r = 122
                g = 193
                b = 240
                colors = 122, 193, 240
            elif result == 'Draw':
                r = 197
                g = 200
                b = 201
                colors = 197, 200, 201
            else:
                r = 222
                g = 82
                b = 87
                colors = 222, 82, 87

            print(f'{colors}')
            embed = discord.Embed(
            title = (f'Result: {result}'),
            description = (f'{player.capitalize()} chose {opponent}!'),
            color = discord.Color.from_rgb(r, g, b)
            )
            await message.channel.send(embed=embed)
        except SyntaxError:
                pass
        except IndexError:
                pass
    await client.process_commands(message)

#@client.event
#async def on_message(message):
#    try:
#        print(message.attachments[0].filename)
#    except IndexError:
#        pass
#    await client.process_commands(message)




client.run(process.env.BOT_TOKEN)
