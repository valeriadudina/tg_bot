from telebot import *
from telebot import types
import config
from DBHandler import to_fill_data, DBHandler
bot=telebot.TeleBot(config.TOKEN)
fields_names = (
    'ID','Имя', 'ИНН', 'СНИЛС', 'Дата начала работы', 'Должность', 'Подразделение', 'Вид зазятости', 'Оклад', 'ФОТ', 'Аванс',
    'График')
@bot.message_handler(commands=['start'])
def first_func(message):
    menu_main = [[types.InlineKeyboardButton('Заполнить поля', callback_data='m1')],
                 [types.InlineKeyboardButton('Option 2', callback_data='m2')],
                 [types.InlineKeyboardButton('Option 3', callback_data='m3')]]
    reply_markup = types.InlineKeyboardMarkup(menu_main)
    #update.message.reply_text('Choose the option:', reply_markup=reply_markup)
    bot.send_message(message.chat.id,
                     "Что вы хотите сделать?",
                     reply_markup=reply_markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call.data)
    if call.data =='m1':
        records = to_fill_data

        menu_data = [[types.InlineKeyboardButton(records[0][1], callback_data=records[0][0])],
                     [types.InlineKeyboardButton(records[1][1], callback_data=records[1][0])],
                     [types.InlineKeyboardButton(records[2][1], callback_data=records[2][0])],
                     [types.InlineKeyboardButton(records[3][1], callback_data=records[3][0])],
                     [types.InlineKeyboardButton(records[4][1], callback_data=records[4][0])],
                     [types.InlineKeyboardButton("Другой сотрудник", callback_data="extra")]]
        reply_markup = types.InlineKeyboardMarkup(menu_data)
        # update.message.reply_text('Choose the option:', reply_markup=reply_markup)
        bot.send_message(call.message.chat.id,
                         "Выберите сотрудника",
                         reply_markup=reply_markup)
    else:
        print(call.data)
        if call.data == 'extra':
            bot.send_message(call.message.chat.id,
                             "Введите ФИО сотрудника")
        else:
            global db_person
            db_person = DBHandler(call.data)
            x = [i for i in range(0, 11) if db_person.fields[i] == '']

            bot.send_message(call.message.chat.id,
                             f"Введите {fields_names[x[0]]} сотрудника")



@bot.message_handler(content_types=['text'])
def fill_data_about_employee(message):
    print("fill data", db_person.fields)
    for i in range (0,11):
        if db_person.fields[i] == '':
            print(db_person.fields[i])
            db_person_list = list(db_person.fields)
            db_person_list[i] = message.text
            db_person.fields = tuple(db_person_list)
            print(db_person.fields)
            break
    x = [i for i in range(0, 11) if db_person.fields[i] == '']
    if x == []:

        ret = db_person.fill_fields()
        print(ret)
        print(db_person.fields)
        bot.send_message(message.chat.id,
                        ret)

    else:
        print('else ', db_person.fields)
        bot.send_message(message.chat.id,
                         f"Введите {fields_names[x[0]]} сотрудника")




#if __name__ == '__main__':
    #bot.polling(none_stop=True)
import requests
import json
import ast
url = "https://api.mindbodyonline.com/public/v6/usertoken/issue"

payload = "{\n  \"username\": \"Yuliyat8819@gmail.com\",\n  \"password\": \"TMkU`8\"q62t5z\\Wm\"\n}"
headers = {
  'Content-Type': 'application/json',
  'API-Key': '7917881a86ea4e048e1aecaedc4cf2da',
  'SiteId': '290740',
  'Cookie': '__cflb=02DiuFkqqzCCQ4gSuJZva1g3X7mH5svx4jHJSToP5PhR6'
}

data= '''{'username': 'Yuliyat8819@gmail.com','password': 'TMkU`8"q62t5z\Wm'}'''
d = ast.literal_eval(data)
print(json.dumps(d))

response = requests.request("POST", url, headers=headers, data=json.dumps(d))

print(response.text)
