import requests
bot_token = '5678917940:AAFadpYE4dAaQ4TzWDtgS1OWpsjRz9m5mvA'


def Telegram_Bot_Sendtext(bot_message):
    bot_chatID = '1211375065'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()