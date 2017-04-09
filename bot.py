import random
import requests
import rlist
import teltoken

URL = "https://api.telegram.org/bot" + teltoken.TOKEN + '/'
LIMIT = 10
TIMEOUT = 10
DOMAIN = 'https://alpha.wallhaven.cc/random'
REDHEAD = 'https://alpha.wallhaven.cc/search?q=ginger'


def get(method, params):
    return requests.get(URL + method, params=params)


def tel_request(method, params):
    response = get(method, params=params)
    return response.json()['result']


def send_message(chat_id, message_id, text):
    return tel_request('sendMessage', params={
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'text': text
    })


def send_sticker(chat_id, message_id, sticker):
    return tel_request('sendSticker', params={
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'sticker': sticker
    })


def rand_sticker(stickerpack):
    rand = random.randint(0, len(stickerpack) - 1)
    return stickerpack[rand]


def ping():
    return send_message(237174923, None, 'OK')


if __name__ == '__main__':

    ping()

    update_id = 0

    while True:

        upd = tel_request('getUpdates', params={
            'limit': LIMIT,
            'timeout': TIMEOUT,
            'offset': update_id + 1})

        for i in upd:
            try:
                chat_id = i['message']['chat']['id']
                message_id = i['message']['message_id']
                text = i['message']['text'].lower()

                if 'test' in text:
                    send_sticker(chat_id, message_id, rand_sticker(rlist.CATS))

            except KeyError:
                pass

        if len(upd) > 0:
            update_id = int(upd[-1]["update_id"])
