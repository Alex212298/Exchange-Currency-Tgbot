import telebot
from config import TOKEN
from extensions import RequestToApi, APIException


bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def com_start(message):
    bot.send_message(message.chat.id, f"Привет *{message.chat.first_name}*! \n"
                                      f"Этот бот помогает обменять валюту. 🤑\n"
                                      f"Введите значение типа: \n"
                                      f"*<Валюта[1]><Валюта[2]><Количество>* \n"
                                      f"Валюта[1] - необходимая к получению \n"
                                      f"Валюта[2] - используемая при обмене \n"
                                      f"Чтобы получить список доступных валют введите — /values ")


@bot.message_handler(commands=['help'])
def com_help(message):
    bot.send_message(message.chat.id, f"Этот бот помогает обменять валюту. 🤑\n"
                                      f"Введите значение типа: \n"
                                      f"*<Валюта[1]><Валюта[2]><Количество>* \n"
                                      f"Валюта[1] - необходимая к получению \n"
                                      f"Валюта[2] - используемая при обмене \n"
                                      f"Чтобы получить список доступных валют введите — /values ")


@bot.message_handler(commands=['values'])
def com_values(message):
    bot.send_message(message.chat.id, "Доступные валюты: RUB, USD, EUR  \n"
                                      "*Рубль \nДоллар \nЕвро*")


@bot.message_handler()
def answer(message):
    list_values = message.text.lower().split()
    response = RequestToApi.get_price(*list_values)
    bot.reply_to(message, text = response)


bot.polling()
