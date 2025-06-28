import logging
import os
from uuid import uuid4
import requests
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Application, InlineQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def format_stats(stats):
    return "\n".join(f"<b>{s['stat']['name'].capitalize()}:</b> {s['base_stat']}" for s in stats)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Thank You for using the Pokédex inline bot.\n\n"
        "a @aBiSerSpeaks initiative"
    )

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query.strip().lower()
    if not query:
        return

    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{query}")
        if response.status_code != 200:
            return
        
        pokemon = response.json()
        name = pokemon['name'].lower()
        pokedex_id = pokemon['id']
        types = ", ".join([t['type']['name'].capitalize() for t in pokemon['types']])
        abilities = ", ".join(
            f"{a['ability']['name'].replace('-', ' ').capitalize()}{' (Hidden)' if a['is_hidden'] else ''}"
            for a in pokemon['abilities']
        )
        base_exp = pokemon['base_experience']
        height = pokemon['height'] / 10  # decimeters to meters
        weight = pokemon['weight'] / 10  # hectograms to kg
        stats = format_stats(pokemon['stats'])
        moves = ", ".join(m['move']['name'].capitalize() for m in pokemon['moves'][:3])

        # Use high-quality image from Pokémon Database
        image_url = f"https://img.pokemondb.net/artwork/{name}.jpg"

        message_text = (
            f"<b>{name.capitalize()} #{pokedex_id}</b>\n"
            f"<b>Type:</b> {types}\n"
            f"<b>Abilities:</b> {abilities}\n"
            f"<b>Base Experience:</b> {base_exp}\n"
            f"<b>Height:</b> {height} m\n"
            f"<b>Weight:</b> {weight} kg\n"
            f"<b>Stats:</b>\n{stats}\n"
            f"<b>Moves:</b> {moves}\n"
            f"<a href='{image_url}'>​</a>"
        )

        results = [InlineQueryResultArticle(
            id=str(uuid4()),
            title=f"{name.capitalize()} #{pokedex_id}",
            description=f"{types} | {abilities}",
            thumbnail_url=image_url,
            input_message_content=InputTextMessageContent(
                message_text=message_text,
                parse_mode='HTML',
                disable_web_page_preview=False
            )
        )]

        await update.inline_query.answer(results)

    except Exception as e:
        logger.error(f"Error fetching Pokémon data: {e}")

def main() -> None:
    # Get the bot token from environment variable
    bot_token = os.environ.get("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN environment variable not set.")

    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(InlineQueryHandler(inline_query))
    application.run_polling()

if __name__ == "__main__":
    main()
