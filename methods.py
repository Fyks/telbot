import requests


# requests get
def get(method, params):
    return requests.get(URL + method, params=params)


# json
def make_request(method, params):
    response = get(method, params=params).json()['result']
    return response


# send message
def send_message(chat_id, message_id, text):
    params = {
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'text': text
    }
    return make_request('sendMessage', params)


# send sticker
def send_sticker(chat_id, message_id, sticker):
    params = {
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'sticker': sticker
    }
    return make_request('sendSticker', params)


def log(text):
    conf_log = open('log1.txt', 'a')
    conf_log.write(username + '\t' + text + '\n')
    conf_log.close()


def ping():
    return send_message(237174923, None, 'OK')

