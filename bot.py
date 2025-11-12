import logging, asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import config

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
log = logging.getLogger(__name__)

# ========= MENSAJES =========
WELCOME_MSG = (
    "💬 *Bienvenido a Telegram P2P PRO*\n\n"
    "💸 Compra o vende USDT de forma segura y anónima.\n"
    "🌐 Abre la WebApp: [telegramp2p.pro](https://telegramp2p.pro)\n"
    "⚡ Conecta tu wallet y envía tu cotización.\n\n"
    f"👤 Contacta a tu agente: [{config.AGENT_USER}](https://t.me/{config.AGENT_USER.lstrip('@')})"
)

MENU_MSG = (
    "⚡ *Centro de operaciones Telegram P2P PRO*\n\n"
    "Selecciona una opción para continuar:"
)

# ========= FUNCIONES =========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💵 Comprar USDT", url=f"{config.OFFICIAL_WEB}")],
        [InlineKeyboardButton("💰 Vender USDT", url=f"{config.OFFICIAL_WEB}")],
        [InlineKeyboardButton("👤 Contactar Agente", url=f"https://t.me/{config.AGENT_USER.lstrip('@')}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(MENU_MSG, parse_mode="Markdown", reply_markup=reply_markup)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MSG, parse_mode="Markdown")

# ========= MAIN =========
def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("comprar", start))
    app.add_handler(CommandHandler("vender", start))
    app.add_handler(CommandHandler("agente", welcome))
    log.info("🤖 Bot conectado y ejecutándose...")
    app.run_polling()

if __name__ == "__main__":
    main()
