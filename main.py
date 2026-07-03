import discord
from discord.ext import commands
from keep_alive import keep_alive
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Tuyul {bot.user} siap tempur buat Summer!')

async def connect_and_scan_gt(world_name):
    
    await asyncio.sleep(3) 
    
    mock_blocks = random.randint(1000, 3000)
    mock_floating = random.randint(0, 150)
    
    return mock_blocks, mock_floating

@bot.command()
async def scan(ctx, world_name: str):
    await ctx.send(f'⏳ masuk ke **{world_name.upper()}** via jalur belakang...')
    
    try:
        total_blocks, total_floating = await connect_and_scan_gt(world_name)
        
        hasil = (f'✅ **Hasil Radar Tuyul: {world_name.upper()}**\n'
                 f'🧱 Total Block Aktif: {total_blocks}\n'
                 f'🎁 Total Tumpukan Floating Item: {total_floating}')
        await ctx.send(hasil)
    except Exception as e:
        await ctx.send(f'Server nolak atau anti-cheat nyala. Error: {e}')

keep_alive()

bot.run('MTUyMjYyNDkyNDUyOTcyMTQyNA.GmO6HR.04NMw2JQtDPOzG3hP6fjJi3LhBrYxQLZjRGszU')
