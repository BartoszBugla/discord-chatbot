import discord
from chat import Chat
from env import DISCORD_TOKEN

BOT_TRIGGER = "!chat"

intents = discord.Intents.default()

intents.message_content = True
intents.guilds = True

bot = discord.Client(intents=intents)

chatbot = Chat()


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        guild_count += 1


@bot.event
async def on_message(message):
    print("Message received")

    if message.content.startswith(BOT_TRIGGER):
        prompt = message.content[len(BOT_TRIGGER) :]

        res = chatbot.invoke(prompt)

        await message.channel.send(res)


bot.run(token=DISCORD_TOKEN)
