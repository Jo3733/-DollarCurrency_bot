import telebot
import requests

bot = telebot.TeleBot('8051662564:AAFy83XwWH2QoulRtV-B-GX8wJTer5Gtbrg')

def get_usd_rate():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()
    return data['Valute']['USD']['Value']

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добрый день. Как вас зовут?")
    bot.register_next_step_handler(message, ask_name)

def ask_name(message):
    name = message.text
    usd_rate = get_usd_rate()
    bot.send_message(message.chat.id, f"Рад знакомству, {name}! Курс доллара сегодня {usd_rate} руб.")

bot.polling(none_stop=True)
