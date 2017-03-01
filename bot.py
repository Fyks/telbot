import requests
import random
import re
import rlist
import teltoken

URL = "https://api.telegram.org/bot" + teltoken.TOKEN + '/'
LIMIT = 10
TIMEOUT = 10


def ping():
    ping = requests.get(URL + 'sendMessage', params={
        'chat_id': 237174923,
        'text': 'Heil cats!'})
    print(ping, 'online')


def response():
    rand = random.randint(0, len(rlist.rlist) - 1)
    answer = rlist.rlist[rand]
    requests.get(URL + 'sendMessage', params={
        'chat_id': chat_id,
        'text': answer,
        'reply_to_message_id': message_id})


def response_pic():
    rand = random.randint(0, len(rlist.ANIME) - 1)
    file_id = rlist.ANIME[rand]
    requests.get(URL + 'sendSticker', params={
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'sticker': file_id})


if __name__ == '__main__':

    ping()

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
                user_id = update['message']['from']['id']

                if re.search(r'Котяш', text):
                    if re.search(r'няш', text):
                        response_pic()
                        break
                    response()

                    print(chat_id, user_id, text)

            except KeyError:
                pass

        if len(get_updates.json()["result"]) > 0:
            last_update_id = int(get_updates.json()["result"][-1]["update_id"])
