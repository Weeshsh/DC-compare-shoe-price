import discord
from discord.ext import commands
from config import CHANNEL, TOKEN
import stockx
import hypeboost
import restocks
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online)
    print("Succesfully logged in!")

@bot.event
async def on_message(message):
    message_content = message.content.lower()
    if message.channel.name == CHANNEL:
        if message_content.startswith('$compare'):
            SKU = message_content.split(' ')[1]
            stckx = stockx.stockx(SKU)
            hpbst = hypeboost.hypeboost(SKU)
            rstcks = restocks.restocks(SKU)
            if stckx != None and hpbst != None and rstcks != None:
                embed = discord.Embed(title = stckx[2],description=f'[Stockx]({stckx[1]}) | [Hypeboost]({hpbst[0]}) | [Restocks]({rstcks[0]})', colour = discord.Color.gold())
                embed.set_footer(text = 'Created by retarded.inc')
                embed.set_thumbnail(url = stckx[0])
                valStockx=''
                valHypeboost=''
                valRestocks=''
                for x in stckx[3]:
                    valStockx += f'{x} | {stckx[3][x]}\n'
                for x in hpbst[1]:
                    valHypeboost += f'{x} | {hpbst[1][x]}\n'
                for x in rstcks[1]:  
                    valRestocks += f'{x} | {rstcks[1][x]}\n'
                embed.add_field(name='Stockx', value=valStockx, inline=True)
                embed.add_field(name='Hypeboost', value=valHypeboost, inline=True)
                embed.add_field(name='Restocks', value=valRestocks, inline=True)
                await message.channel.send(embed = embed)
                print('Message Sent!')
            else:
                print('Error sending the message')

bot.run(TOKEN)