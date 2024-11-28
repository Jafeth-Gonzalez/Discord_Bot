import discord
from discord.ext import commands
import random
import google.generativeai as genai

genai.configure(api_key="yor api")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$',  intents=intents)



@bot.command()
async def gemini(ctx, *, query: str):
    async with ctx.typing():
        response = model.generate_content(query)
        await ctx.send(f"Gemini: {response.text}")

@bot.command()
async def comandos(ctx):
    commands_list = "\n".join([f"- `{command.name}`: {command.help or 'Sin descripción' }" for command in bot.commands])
    await ctx.send(f"Lista de comandos disponibles:\n{commands_list}")
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


bot.run("your token")