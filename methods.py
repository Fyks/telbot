import requests


# requests get
def get(url, method, params):
    return requests.get(url + method, params=params)


# json
def make_request(url, method, params):
    response = get(url, method, params=params).json()['result']
    return response


# send message
def send_message(url, chat_id, message_id, text):
    params = {'chat_id': chat_id,
              'reply_to_message_id': message_id,
              'text': text}
    return make_request(url, 'sendMessage', params)


# send sticker
def send_sticker(url, chat_id, message_id, sticker):
    params = {'chat_id': chat_id,
              'reply_to_message_id': message_id,
              'sticker': sticker}
    return make_request(url, 'sendSticker', params)


def log(username, text):
    conf_log = open('log1.txt', 'a')
    conf_log.write(username + '\t' + text + '\n')
    conf_log.close()


def ping(url):
    return send_message(url, 237174923, None, 'Ready')

