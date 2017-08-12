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


# done
def timer():
    t = time.gmtime()[:]
    suspend_time = time.mktime(t[:4] + (t[4]+3,) + t[5:])
    return suspend_time


# done
def checker(message):
    if 'mute' in message['text'].lower():
        user_id = message['from']['id']
        if message['reply_to_message']['from']['id']:
            reply_id = message['reply_to_message']['from']['id']
            return [{user_id: reply_id}, timer()]


# done
def del_message(chat_id, message_id):
    params = {'chat_id': chat_id,
              'message_id': message_id}
    return requests.get('deleteMessage', params)
