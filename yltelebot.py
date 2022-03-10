from telegram.ext import Updater, Dispatcher
from telegram.ext import CommandHandler, MessageHandler
import os

TOKEN = os.environ['TELEGRAMID']

def start(update, context):
    yourname = update.message.chat.first_name
    msg = "Hi" + yourname +"!"
    context.bot.send_message(update.message.chat.id, msg)

def error(update, context):
    context.bot.send_message(update.message.chat.id, "Command not recognised")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=os.environ.get("PORT", 8443), url_path=TOKEN, webhook_url="https://yltestbot.herokuapp.com/"+TOKEN)
    updater.idle()

if __name__=='__main__':
    main()
