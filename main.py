from telegram import Bot
import os
token=os.environ["TELEGRAM_BOT_TOKEN"]
from telegram.ext import ApplicationBuilder, CommandHandler
async def start(update, context):
  await update.message.reply_text("Baba Yaga está online.")

def main():
  application = ApplicationBuilder().token(token).build()
  application.add_handler(CommandHandler("start", start))
                        
  application.run_polling()
if __name__ == "__main__":
  main()
