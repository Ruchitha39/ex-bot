import discord

# Intents are required for receiving message events
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Prevent bot from replying to itself
    if message.author == client.user:
        return

    # Echo the message back
    await message.channel.send(message.content)

# Insert your bot token below
client.run('enter your bot api')
