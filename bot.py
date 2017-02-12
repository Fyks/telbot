import requests
import random
import re

TOKEN = "256779559:AAG_j5feHZhxQXYkeUIKviqKMsPRaoVhv30"
URL = "https://api.telegram.org/bot" + TOKEN + '/'
LIMIT = 10
TIMEOUT = 10
damnlist = ['Няк?', '*пускаю искры*', '*подпрыгнул*',
            '*вылизываю промежность*', '*purr purr*',
            '*ищу взглядом твою обувь*', '*смотрю в сторону*',
            '*убегаю*', '*смотрю в пустой угол*', '*зашипел*',
            '*свернулся клубочком*', 'Может погладишь, сука?',
            'Только поел, перестань', 'Давно обувь менял?',
            'Это потому что ты - няша', 'Что еще някнешь?',
            'Хорошего дня, няша!', 'Возможно ты прав',
            'Не имей сто друзей, а имей сто котов', 'А?',
            'Я тебе потом отвечу', 'Лениво отвечать',
            'Твоя мама - хорошая женщина', 'Твой папа - достойный мужчина']


def ping():
    ping = requests.get(URL + 'sendMessage', params={
        'chat_id': 237174923,
        'text': 'Heil cats!'})
    print(ping, 'online')


def responce():
    rand = random.randint(0, len(damnlist) - 1)
    answer = damnlist[rand]
    requests.get(URL + 'sendMessage', params={
        'chat_id': chat_id,
        'text': answer,
        'reply_to_message_id': message_id})


ping()


if __name__ == '__main__':

    last_update_id = 0

    while True:

        get_updates = requests.get(URL + 'getUpdates', params={
            'limit': LIMIT,
            'timeout': TIMEOUT,
            'offset': last_update_id + 1})

        for update in get_updates.json()['result']:
            try:
                chat_id = update['message']['chat']['id']
                message_id = update['message']['message_id']
                text = update['message']['text']
                user = update['message']['from']['username']

                if re.search(r'Котяш', text):
                    responce()

                print(chat_id, user, text)

            except KeyError:
                pass

        if len(get_updates.json()["result"]) > 0:
            last_update_id = int(get_updates.json()["result"][-1]["update_id"])
