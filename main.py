from telegram import Bot
import os
token=os.environ["TELEGRAM_BOT_TOKEN"]
from telegram.ext import ApplicationBuilder, CommandHandler
async def start(update, context):
  await update.message.reply_text("Baba Yaga está online.")

def main():
  application = Application.Builder().token(token).build()
  application.edd_handler(CommandHandler("start", start))
                        
  application.ram_polling()
if __name__ == "__main__"..
  main()
