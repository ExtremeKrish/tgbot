import requests

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}

    response = requests.post(url, params=params)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with your actual bot token and user chat ID
bot_token = '6171891363:AAEgSTM5I5w2ljZEl4uJ6cdgFmHJWqnHOmQ'
chat_id = '6162808595'
message_text = 'Hello, this is a test message from your Telegram bot!'

send_telegram_message(bot_token, chat_id, message_text)
