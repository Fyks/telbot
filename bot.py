import random
import requests
import teltoken
import blacklist
import parcer

URL = "https://api.telegram.org/bot" + teltoken.TOKEN + '/'
LIMIT = 10
TIMEOUT = 10


def get(method, params):
    return requests.get(URL + method, params=params)


def request(method, params):
    response = get(method, params=params).json()['result']
    return response


def send_message(chat_id, message_id, text):
    params = {
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'text': text
    }
    return request('sendMessage', params)


def send_sticker(chat_id, message_id, sticker):
    params = {
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'sticker': sticker
    }
    return request('sendSticker', params)


def rand_sticker(stickerpack):
    rand = random.randint(0, len(stickerpack) - 1)
    return stickerpack[rand]


def log(text):
    conf_log = open('log1.txt', 'a')
    conf_log.write(username + '\t' + text + '\n')
    conf_log.close()


def ping():
    return send_message(237174923, None, 'OK')


if __name__ == '__main__':

    ping()

    update_id = 0

    while True:

        upd = request('getUpdates', params={
            'limit': LIMIT,
            'timeout': TIMEOUT,
            'offset': update_id + 1})

        for i in upd:
            try:
                chat_id = i['message']['chat']['id']
                message_id = i['message']['message_id']
                username = i['message']['from']['first_name']
                text = i['message']['text'].lower()
                log(text)
                print(username, text)

                if text in blacklist.black_list:
                    send_message(chat_id, message_id, 'хуйня')
                if 'gimme' in text:
                    try:
                        link = parcer.domain_modifier(text)
                        send_message(chat_id, message_id,
                                     parcer.final_link(link))
                    except ValueError:
                        send_message(chat_id, message_id,
                                     'Not found ¯\\_(ツ)_/¯')

            except KeyError:
                print('Key_error')
                pass

        if len(upd) > 0:
            update_id = int(upd[-1]["update_id"])
