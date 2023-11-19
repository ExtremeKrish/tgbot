from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6629025964:AAEx3-t_AmAy-vGK3Gk0JH2f7a61EisDxsk'

def repeat_message(update, context):
    user_input = update.message.text
    update.message.reply_text(f"You said: {user_input}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Register a message handler to respond to text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, repeat_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
