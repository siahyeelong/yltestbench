from telegram.ext import Updater, Dispatcher
from telegram.ext import CommandHandler, MessageHandler
from telegram import *
from telegram.ext import *
import os

TOKEN = os.environ['TELEGRAMID']

def start(update, context):
    yourname = update.message.chat.first_name
    msg = "Hi " + yourname +"! Welcome to YL's test bot. To begin, type /help to see what you can do"
    context.bot.send_message(update.message.chat.id, msg)
    
def help(update, context):
    msg = "(work in progress)"
    context.bot.send_message(update.message.chat.id, msg)
    
def new(update, context):
    ar0 = str(context.args[0])
    ar1 = str(" ".join(context.args[1:])
    msg = "argument 0 = {} \nargument 1 = {}".format(ar0, ar1)
    context.bot.send_message(update.message.chat.id, msg)

def error(update, context):
    context.bot.send_message(update.message.chat.id, "Command not recognised")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("new", new))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=os.environ.get("PORT", 8443), url_path=TOKEN, webhook_url="https://yltestbot.herokuapp.com/"+TOKEN)
    updater.idle()

if __name__=='__main__':
    main()
