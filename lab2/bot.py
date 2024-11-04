import telebot
from telebot import types
import requests
from urllib.request import urlopen

bot = telebot.TeleBot('SecretCode')
#ask @tal3nt3d on telegram to get it

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row("/help")
    bot.send_message(message.from_user.id, "Привет, меня зовут WeatherBot, и я показываю погоду в заданном месте\nНапиши /help, чтобы узнать мои команды", reply_markup=user_markup)

@bot.message_handler(content_types=['text', 'document', 'audio', ])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Вот список моих команд: \nПогода - узнать погоду в указанном городе в данный момент\nПрогноз погоды - узнать погоду в указанном городе через несколько дней\nСтоп - остановить бота\n")
        keyboard = types.InlineKeyboardMarkup()
        key_weather = types.InlineKeyboardButton(text='Погода сейчас', callback_data='weather')
        keyboard.add(key_weather)
        key_forecast = types.InlineKeyboardButton(text='Прогноз погоды', callback_data='forecast')
        keyboard.add(key_forecast)
        key_stop = types.InlineKeyboardButton(text='Стоп', callback_data='stop')
        keyboard.add(key_stop)
        bot.send_message(message.from_user.id, text='Выбери действие:', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func = lambda call:True)
def callback_worker(call):
    if call.data == "stop":
        bot.send_message(call.message.chat.id, "Бот остановлен")
        bot.stop_bot()
    if call.data =="weather":
        get_city(call.message)
    if call.data == "forecast":
        get_forecast(call.message)

def get_request(message, days = 1):
    key = '0c1af30537bd45d6881120213241809'
    adress = 'http://api.weatherapi.com/v1/'
    if days != 1:
        adress += 'forecast.json?key=' + key + '&q=' + message.text + '&days=' + str(days) + '&aqi=no&alerts=no'
    else:
        adress += 'current.json?key=' + key + '&q=' + message.text + '&aqi=no'
    r = requests.get(adress)
    data = r.json()
    return data

@bot.message_handler(content_types=['text'])
def get_city(message):
    q = bot.send_message(message.chat.id, "В каком городе показать погоду?")
    bot.register_next_step_handler(q, say_weather)

def say_weather(message):
    data = get_request(message)
    response = "Температура в городе " + data['location']['name'] + " - " + str(data['current']['temp_c']) + "°C градусов по Цельсию\nВлажность в городе " + data['location']['name'] + " - " + str(data['current']['humidity']) + "%"
    bot.send_message(message.chat.id, response)
    photo = data['current']['condition']['icon']
    photo = urlopen('https:' + photo)
    bot.send_photo(message.chat.id, photo)
    
@bot.message_handler(content_types=['text'])    
def get_forecast(message):
    q = bot.send_message(message.chat.id, "В каком городе показать прогноз погоды?")
    bot.register_next_step_handler(q, get_days)

def get_days(message):
    days = bot.send_message(message.chat.id, "На сколько дней показать прогноз?")
    bot.register_next_step_handler(days, say_forecast, message)
    
def say_forecast(days, message):
    cnt = int(days.text)
    data = get_request(message, cnt)
    for i in range(0, cnt):
        date = str(data['forecast']['forecastday'][i]['date'])
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        date = day + '.' + month + '.' + year
        response = date + ' в городе ' + data['location']['name'] + ' максимальная температура будет достигать ' + str(data['forecast']['forecastday'][i]['day']['maxtemp_c']) + '°C градусов по Цельсию, а'\
        ' минимальная температура будет опускаться до ' + str(data['forecast']['forecastday'][i]['day']['mintemp_c']) + '°C градусов по Цельсию!'
        bot.send_message(message.chat.id, response)

bot.polling(none_stop=True, interval=0)
