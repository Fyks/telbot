import requests
import time

mute_list = {}
mute_count = {}
mute_timer = {}


def restrict_user(chat_id, user_id, can_send_messages=None, can_send_media_messages=None,
                  can_send_other_messages=None, until_date=None):
    params = {'chat_id': chat_id,
              'user_id': user_id,
              'until_date': until_date,
              'can_send_messages': can_send_messages,
              'can_send_media_messages': can_send_media_messages,
              'can_send_other_messages': can_send_other_messages}
    return requests.get('restrictChatMember', params)


def mute_counter(message, list):
    if 'mute' in message['text'].lower():
        if message['reply_to_message']['from']['id']:
            abuse_id = message['from']['id']
            if abuse_id in list:
                print('NO')
            else:
                list[message['from']['id']] = message['reply_to_message']['from']['id']
                print('gotcha')
                return list
    else:
        pass


def timer(text):
    if 'mute' in text:
        current_timedate = time.gmtime()[:]

        return t
