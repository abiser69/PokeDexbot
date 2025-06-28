Here's a complete Python code for an inline Telegram bot using `python-telegram-bot` that fetches Pokémon data from PokeAPI.co:

## Key Features:
1. **Inline Search**: Users type `@YourBotName pokemon_name` in any chat
2. **Pokémon Data Includes**:
   - Official artwork image
   - Pokémon name and ID
   - Type(s)
   - Top 3 abilities
3. **Rich Formatting**: Uses HTML formatting for better display
4. **Error Handling**: Gracefully handles invalid Pokémon names

## Setup Instructions:
1. Install required packages:
```bash
pip install python-telegram-bot requests
```

2. Replace `BOT_TOKEN` with your actual bot token from @BotFather

3. Enable inline mode with @BotFather:
   - Send `/setinline` to @BotFather
   - Select your bot
   - Set an inline placeholder (e.g., "Search Pokémon...")
   - 
To use your bot token from a virtual environment, you should store it in an environment variable (e.g., `TELEGRAM_BOT_TOKEN`).  
You can then retrieve it in your code using Python’s `os.environ`.




## How to use a virtual environment and set your token

1. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
    ```

2. **Install dependencies:**
    ```bash
    pip install python-telegram-bot requests
    ```

3. **Set your bot token as an environment variable:**

    - **On Linux/Mac:**
      ```bash
      export TELEGRAM_BOT_TOKEN=your-telegram-bot-token
      ```
    - **On Windows (CMD):**
      ```cmd
      set TELEGRAM_BOT_TOKEN=your-telegram-bot-token
      ```
    - **On Windows (PowerShell):**
      ```powershell
      $env:TELEGRAM_BOT_TOKEN="your-telegram-bot-token"
      ```

4. **Run your bot:**
    ```bash
    python your_bot_file.py
    ```

Now your bot token is securely managed via your virtual environment!



## Usage:
1. In any Telegram chat, type `@YourBotName pikachu`
2. Select the result from the popup menu
3. The bot will post the Pokémon information in the chat

## Example Output (for Pikachu):
```
Pikachu #25
Type: electric
Abilities: static, lightning-rod
[Image of Pikachu]
```

This implementation uses PokeAPI's RESTful interface to fetch Pokémon data in real-time and formats it for optimal display in Telegram. The inline mode provides a seamless user experience without requiring users to start a chat with the bot.



