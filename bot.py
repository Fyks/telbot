import random
import re
import requests
import rlist
import teltoken

URL = "https://api.telegram.org/bot" + teltoken.TOKEN + '/'
LIMIT = 10
TIMEOUT = 10


def get(method, params):
    return requests.get(URL + method, params=params)


def tel_request(params):
    response = get('getUpdates', params=params)
    return response.json()['result']


def send_message(chat_id, reply_to_message_id):
    get('sendMessage', params={
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'text': rand_text()
    })


def send_sticker(chat_id, reply_to_message_id):
    get('sendSticker', params={
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'sticker': rand_sticker()
    })


def rand_sticker():
    rand = random.randint(0, len(rlist.ANIME) - 1)
    sticker = rlist.ANIME[rand]
    return sticker


def rand_text():
    rand = random.randint(0, len(rlist.rlist) - 1)
    text = rlist.rlist[rand]
    return text


def ping():
    get('sendMessage', params={
        'chat_id': 237174923,
        'text': 'OK'
    })


if __name__ == '__main__':

    ping()

    update_id = 0

    while True:

        upd = tel_request(params={
            'limit': LIMIT,
            'timeout': TIMEOUT,
            'offset': update_id + 1})

        for i in upd:
            try:
                chat_id = i['message']['chat']['id']
                message_id = i['message']['message_id']
                text = i['message']['text']

                if re.search(r'Котяш', text):
                    if re.search(r'няш', text):
                        send_sticker(chat_id, message_id)
                        break
                    send_message(chat_id, message_id)
            except KeyError:
                pass

        if len(upd) > 0:
            update_id = int(upd[-1]["update_id"])
