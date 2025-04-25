# Ex AI Chatbot Discord Bot

## Overview

**Ex AI Chatbot** is a Discord bot that utilizes the Gemini AI model to provide intelligent and engaging responses. The bot can respond to user queries, offer helpful information, and deliver fun, friendly interactions with a touch of humor when appropriate. It supports long responses, automatically splitting them into a text file if the message exceeds Discord's message length limit.

## Features

- **AI-Powered Responses**: The bot uses the Gemini AI model to generate accurate and informative responses to user queries.
- **Friendly & Engaging**: The bot's responses are designed to be helpful, with a friendly and approachable tone.
- **Text File Support**: If the response is too long for Discord's message limit, the bot will send the response as a text file.
- **Error Handling**: The bot gracefully handles long responses, encoding issues, and other errors to ensure smooth interaction.

## Installation

To run the bot, you'll need to have Python installed and create a virtual environment. Follow the steps below to get started:

### Prerequisites

- Python 3.7 or higher
- A Discord bot token (create one from the [Discord Developer Portal](https://discord.com/developers/applications))
- A Gemini API key (from Google Cloud's Gemini platform)

### Steps to Set Up

1. **Clone the repository or create your bot file:**

   Clone the repository (or simply copy the Python script to your local machine).

   ```bash
   git clone https://github.com/your-username/ex-ai-chatbot.git
   cd ex-ai-chatbot
   ```

2. **Install the required dependencies:**

   Use `pip` to install the required libraries. It is recommended to use a virtual environment to keep dependencies isolated.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Add your API Keys:**

   - Replace the placeholder `YOUR_GEMINI_API_KEY` in the script with your actual Gemini API key.
   - Replace the placeholder `YOUR_DISCORD_BOT_TOKEN` with your Discord bot token.

4. **Run the bot:**

   Start the bot by running the Python script:

   ```bash
   python bot_google_ai.py
   ```

   The bot will log in to Discord and be ready to interact with users.

## Commands

- **!ask [question]**: Ask the bot any question starting with `!ask`. The bot will generate a response based on the Gemini AI model.
- **Bot Mention**: You can also mention the bot (`@Ex AI Chatbot`) to ask a question.

## Example

- **User**: `!ask What's the weather today?`
- **Bot**: Responds with a detailed message based on the Gemini AI model.

## Error Handling

If the bot's response exceeds Discord's 2000-character limit, the bot will send the response as a `.txt` file, ensuring that all information is delivered to the user. The bot also gracefully handles encoding issues, ensuring that all characters, including emojis, are properly processed.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are always welcome!

### Bug Reports and Issues

If you encounter any bugs or issues, please open an issue in the [GitHub repository](https://github.com/Ruchitha39/ex-bot/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
