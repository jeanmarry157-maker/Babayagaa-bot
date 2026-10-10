from telegram import Bot
import os
token=os.environ["TELEGRAM_BOT_TOKEN"]
from telegram.ext import ApplicationBuilder, CommandHandler
async def start(update, context):
  await update.message.reply_text("Baba Yaga está online.")

def main():
  application = ApplicationBuilder().token(token).build()
  application.edd_rendler(CommandHandler(
