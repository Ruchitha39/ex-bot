import discord
import requests
import json

# --- Discord Setup ---
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# --- OpenRouter API Setup ---
OPENROUTER_API_KEY = "enter your api key"
MODEL = "nvidia/llama-3.1-nemotron-nano-8b-v1:free"

def query_openrouter(user_message):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
            })
        )

        if response.status_code == 200:
            ai_reply = response.json()['choices'][0]['message']['content']
            return ai_reply
        else:
            return f"⚠ API Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f" Exception occurred: {str(e)}"

# --- Discord Events ---

@client.event
async def on_ready():
    print(f' Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Optional: Only reply if user tags the bot or starts with a command prefix
    if client.user.mentioned_in(message) or message.content.startswith("!ask"):
        user_input = message.content.replace(f"<@{client.user.id}>", "").replace("!ask", "").strip()

        if not user_input:
            await message.channel.send("💬 Please enter a question or message.")
            return

        await message.channel.send("⏳ Thinking...")

        reply = query_openrouter(user_input)

        # Send with Markdown formatting
        await message.channel.send(f"```markdown\n{reply}\n```")

# --- Run Your Bot ---
client.run("enter your bot api key")
