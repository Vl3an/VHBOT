# bot.py
import os
import random
from dotenv import load_dotenv
import discord
import threading
import time
from discord.ext import commands
import os 
from math import *
import signal 
import re
import signal


#vars
TOKEN = 'NjkyNDQyNzkyNTk2NjAyOTYw.Xn3ZHQ.wXIER0ICfgdUYoJqXEf4DSvflnA'
bot = commands.Bot(command_prefix='!')
client = discord.Client()
boomers = ['Rémi Gouillardon']
classe = ['Titouan Burgunder', 'mathieu222', 'SPCMyster', 'Maxime Paulin', 'Prillard Hugo', 'Lorris Collette', 'BaptistASMR', 'Celsius', 'Yass', 'RomainDupre', 'Eloïse 2', 'Chloé CORNU', 'Paul A', 'Benoît Morey', 'Lémia', 'illana', 'Bright', 'Erendoudouille', 'Castor Joufflu', 'Maxence Colin', 'Ryan_R', 'Quentin', '6tèmesolaire', 'Clément Jacquemin-V', 'Louise Fumey', 'Vincent belpois', 'Jeanne Grevillot', 'Zokar', 'Vl3an', 'EsteLaTerreur', 'Rémi Gouillardon', 'OTH', 'manon girod', 'dorian guerin', 'Romain Viennet', 'Thomas HILDENBRAND', 'Zalioso', 'Unnerf_raza', 'YanisOuamrane', 'Emeline Jacquey']
poems = ["On passe une moitié de sa vie à attendre ceux qu'on aimera et l'autre moitié à quitter ceux qu'on aime.",
        "On ne souffre jamais que du mal que nous font ceux qu'on aime. Le mal qui vient d'un ennemi ne compte pas.",
        "Une femme qu'on aime est toute une famille.",
        "Le bonheur est parfois caché dans l'inconnu.",
        "Mieux vaut une conscience tranquille qu'une destinée prospère. J'aime mieux un bon sommeil qu'un bon lit.",
        "Enfer chrétien, du feu. Enfer païen, du feu. Enfer mahométan, du feu. Enfer hindou, des flammes. A en croire les religions, Dieu est né rôtisseur.",
        "L'éducation, c'est la famille qui la donne ; l'instruction, c'est l'Etat qui la doit.",
        "Je crois ce que je dis, je fais ce que je crois.",
        "La véritable indulgence consiste à comprendre et à pardonner les fautes qu'on ne serait pas capable de commettre.",
        "Mes amis, retenez ceci, il n'y a ni mauvaises herbes ni mauvais hommes. Il n'y a que de mauvais cultivateurs.",
        "La liberté commence où l'ignorance finit.",
        "Il y a souvent plus de choses naufragées au fond d'une âme qu'au fond de la mer.",
        "La mélancolie, c'est le bonheur d'être triste.",
        "Quand je suis triste, je pense à vous, comme l'hiver on pense au soleil, et quand je suis gai, je pense à vous, comme en plein soleil on pense à l'ombre.",
        "Lire, c'est boire et manger. L'esprit qui ne lit pas maigrit comme le corps qui ne mange pas.",
        "La musique est la vapeur de l'art. Elle est à la poésie ce que la rêverie est à la pensée, ce que le fluide est au liquide, ce que l'océan des nuées est à l'océan des ondes.",
        "Rien n'est stupide comme vaincre ; la vraie gloire est convaincre.",
        "N'imitez rien ni personne. Un lion qui copie un lion devient un singe.",
        "Une femme qui a un amant est un ange, une femme qui a deux amants est un monstre, une femme qui a trois amants est une femme.",
        "Quand le peuple sera intelligent, alors seulement le peuple sera souverain.",
        "L'amour d'une famille, le centre autour duquel tout gravite et tout brille.",
        "Et de l'union des libertés dans la fraternité des peuples naîtra la sympathie des âmes, germe de cet immense avenir où commencera pour le genre humain la vie universelle et que l'on appellera la paix de l'Europe.",
        "Aucune grâce extérieure n'est complète si la beauté intérieure ne la vivifie. La beauté de l'âme se répand comme une lumière mystérieuse sur la beauté du corps.",
        "Faire rire, c'est faire oublier. Quel bienfaiteur sur la terre, qu'un distributeur d'oubli !",
        "Ceux qui vivent sont ceux qui luttent.",
        "Celui qui ouvre une porte d'école, ferme une prison."]

#bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game('vh!help'))


@bot.event
async def on_message(message):
    print(f"{message.channel} | {message.author} : {message.content}")
    if (("*" in message.content) or ("+" in message.content) or ("-" in message.content) or ("/" in message.content)) and (not 'VH Bot' in str(message.author)):
        text = message.content
        if (re.search(r"[0-9]{2,}\*\*[0-9]{3,}",text) is None) and (re.search(r"[0-9]{3,}\*\*[0-9]{2,}",text) is None):
            try: 
                embed = discord.Embed(title='Calculs',colour=discord.Color.from_rgb(0,255,0))
                embed.add_field(name=text, value=str(eval(text)))
                await message.channel.send(content = None, embed = embed)
            except ZeroDivisionError as error:
                embed = discord.Embed(title='Calculs',colour=discord.Color.from_rgb(255,0,0))
                embed.add_field(name=text, value='Division par 0')
                await message.channel.send(content = None, embed = embed)
            except:
                pass
        else:
            embed = discord.Embed(title='Calculs',colour=discord.Color.from_rgb(255,0,0))
            embed.add_field(name=text, value='Trop de puissances.')
            await message.channel.send(content = None, embed = embed)

    if "vh!appel" in message.content or 'vh! appel' in message.content:
        try:
            channel = message.author.voice.channel
        except AttributeError:
            embed = discord.Embed(title='Appel',colour=discord.Color.from_rgb(255,0,0))
            embed.add_field(name='Erreur', value="Vous devez etre dans un channel vocal pour faire l'appel")
            await message.channel.send(content = None, embed = embed)
        absents = []
        for name in classe:
            if not discord.utils.get(message.guild.members, name=name) in channel.members:
                if discord.utils.get(message.guild.members, name=name).nick is not None:
                    absents.append(discord.utils.get(message.guild.members, name=name).nick)
                else:
                    absents.append(discord.utils.get(message.guild.members, name=name).name)
        
        if len(absents) != 0:
            embed = discord.Embed(title="Appel",colour=discord.Color.from_rgb(255,0,0))
            embed.add_field(name=f"Absents : {len(absents)}", value=str(absents))
        elif len(absents) == 0:
            embed = discord.Embed(title="Appel",colour=discord.Color.from_rgb(0,255,0))
            embed.add_field(name="Absents", value='Aucun')
        await message.channel.send(content = None,embed = embed )
    
    if "vh!citation" in message.content:
        poem = random.choice(poems)
        embed = discord.Embed(title='Citation',colour=discord.Color.from_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        embed.add_field(name='"' + poem + '"',value ='Victor Hugo')
        await message.channel.send(content = None, embed = embed)
    if "vh!help" in message.content:
        embed = discord.Embed(title='Help',colour=discord.Color.from_rgb(255,128,0))
        embed.add_field(name='vh!citation',value ='Vous donne une de mes citations.')
        embed.add_field(name='vh!appel',value ="Fait l'appel dans un salon vocal.")
        embed.add_field(name='vh!help',value ='Je réecris ce message...')
        embed.add_field(name='<calcul>',value ="J'éxécute sans tarder le calcul demandé.")
        await message.channel.send(content = None, embed = embed)
        

"""
@bot.event
async def on_member_update(before,after):
    if not after.nick in classe or not after.name in classe:
        lastnick = before.nick
        await after.edit(nick = lastnick)
"""
        



@bot.command
async def boomeradd(ctx):
    name = str(ctx.message)[12:]
    print(name)
    if (not name in boomers):
        boomers.append(name)
    else:
        boomers.remove(name)
    await ctx.message.channel.send(str(boomers))

@bot.event
async def on_reaction_add(reaction,user):
    print(f"{reaction.message.channel} | {user} added a reaction")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('This command does not exist')

bot.run(TOKEN)
