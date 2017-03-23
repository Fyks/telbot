import parcer
import random
import re
import requests
import rlist
import teltoken

URL = "https://api.telegram.org/bot" + teltoken.TOKEN + '/'
LIMIT = 10
TIMEOUT = 10
DOMAIN = 'https://alpha.wallhaven.cc/search?q=urban&categories=111&purity=110&sorting=random&order=desc&page=2'


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


def rand_anime_sticker():
    rand = random.randint(0, len(rlist.ANIME) - 1)
    return rlist.ANIME[rand]


def rand_cat_sticker():
    rand = random.randint(0, len(rlist.CATS) - 1)
    return rlist.CATS[rand]


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

                if re.search(r'test', text):
                    if re.search(r'hi', text):
                        send_sticker(chat_id, message_id, rlist.HI)
                        break
                    elif re.search(r'sticker', text):
                        send_sticker(chat_id, message_id, rand_cat_sticker())
                        break
                    elif re.search(r'pic', text):
                        send_message(chat_id, message_id,
                                     parcer.final_link(DOMAIN))
                        break

                    send_sticker(chat_id, message_id, rand_cat_sticker())

            except KeyError:
                pass

        if len(upd) > 0:
            update_id = int(upd[-1]["update_id"])
