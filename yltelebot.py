from telegram.ext import Updater, Dispatcher
from telegram.ext import CommandHandler, MessageHandler
import os

#TOKEN = os.environ.get("TELEGRAMID")
TOKEN = "5259967950:AAEbvHnIzvBnq1JYvEvL0R-fZP4BkevW7ew"

def start(update, context):
    yourname = update.message.chat.first_name
    msg = "Hi" + yourname +"!"
    context.bot.send_message(update.message.chat.id, msg)

def error(update, context):
    context.bot.send_message(update.message.chat.id, "Command not recognised")

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.Dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=os.environ.get("PORT", 443), url_path=TOKEN, webhook_url="https://yltestbench.heroku.com/"+TOKEN)
    updater.idle()

if __name__=='__main__':
    main()
