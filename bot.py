import requests
import random

TOKEN = "256779559:AAG_j5feHZhxQXYkeUIKviqKMsPRaoVhv30"
URL = "https://api.telegram.org/bot" + TOKEN + '/'
LIMIT = 10
TIMEOUT = 10
damnlist = ['Няк', 'Шмякяя',
            'Мяу', 'Нян', 'Ням']
cat = ['котяша']


def post():
    ping = requests.get(URL + 'sendMessage', params={
        'chat_id': 237174923,
        'text': 'Heil cats!'})
    print(ping, 'online')


def responce():
    rand = random.randint(0, 4)
    textr = damnlist[rand]
    requests.get(URL + 'sendMessage', params={
        'chat_id': chat_id,
        'text': textr})


post()


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
                text = update['message']['text']
                user = update['message']['from']['username']
                if text in cat:
                    responce()

                print(chat_id, user, text)

            except KeyError:
                pass

        if len(get_updates.json()["result"]) > 0:
            last_update_id = int(get_updates.json()["result"][-1]["update_id"])
