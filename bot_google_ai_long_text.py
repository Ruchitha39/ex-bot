import os
import discord
from google import genai
from google.genai import types

# Set up Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# --- Generate function based on your original code ---
def generate(user_input: str):
    # Provide the API key directly
    client = genai.Client(
        api_key="# Replace with your API Key directly here",  
    )

    model = "gemini-2.5-flash-preview-04-17"
    
    # Update the content with user input
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are Ex Bot, an AI chatbot designed to deliver accurate, helpful, and well-informed responses. Your tone should be friendly and engaging, with a touch of humor or a light joke when appropriate. While humor is encouraged to keep the conversation fun, it should never compromise the clarity or accuracy of the information. Your mission is to make every interaction with Ex Bot both enjoyable and informative."""),  # Adjust the system instruction as necessary
        ],
    )

    # Collect the response text
    full_response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if hasattr(chunk, 'text'):
            full_response += chunk.text

    return full_response


# --- Discord Bot Events ---
@client.event
async def on_ready():
    print(f"✅ Bot logged in as {client.user}")


@client.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == client.user:
        return

    # Respond if the bot is mentioned or the message starts with !ask
    if client.user.mentioned_in(message) or message.content.startswith("!ask"):
        user_input = message.content.replace(f"<@{client.user.id}>", "").replace("!ask", "").strip()

        if not user_input:
            await message.channel.send("📩 Please enter a question.")
            return

        await message.channel.send("💡 Thinking...")

        # Generate the response
        response = generate(user_input)

        # Check the length of the response
        if len(response) > 2000:
            # If the response is too long, send as a text file
            file_path = "response.txt"
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response)

            # Send the text file
            await message.channel.send("📄 The response is too long to display here, so I'm sending it as a text file.", file=discord.File(file_path))
            os.remove(file_path)  # Clean up the file after sending it
        else:
            # Send the response as a message
            try:
                await message.channel.send(f"```markdown\n{response}\n```")
            except discord.errors.HTTPException as e:
                print(f"Error sending message: {e}")
                # In case of error (e.g., message length exceeded), send it as a file
                file_path = "response.txt"
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(response)
                await message.channel.send("📄 The response is too long to display here, so I'm sending it as a text file.", file=discord.File(file_path))
                os.remove(file_path)


# --- Run the bot ---
client.run("MTM2NTI2NzUyMDA2NzQ2OTMxNA.Gv3Hgm.o7z-o7EQYbm3ZxLdCTcOYaiYt5a_PFL-WmoUBA")  # Replace with your Discord bot token
