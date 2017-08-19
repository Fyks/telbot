import methods
import requests
import teltoken
import time

mute_list = {}
mute_count = {}
mute_timer = {}
URL = 'https://api.telegram.org/bot' + teltoken.TOKEN + '/'


# restrict method
def restrict_user(chat_id, user_id, until_date=None, can_send_messages=None, can_send_media_messages=None,
                  can_send_other_messages=None, can_add_web_page_previews=None):
    params = {'chat_id': chat_id,
              'user_id': user_id,
              'until_date': until_date,
              'can_send_messages': can_send_messages,
              'can_send_media_messages': can_send_media_messages,
              'can_send_other_messages': can_send_other_messages,
              'can_add_web_page_previews': can_add_web_page_previews}
    return requests.get(URL + 'restrictChatMember', params)


# return current unix time + 3 min
def timestamp():
    t = time.gmtime()[:]
    suspend_time = time.mktime(t[:4] + (t[4]+3,) + t[5:])
    return int(suspend_time)


# checker
def checker(message, mute_list):
    if 'mute' in message['text'].lower():
        muter = message['from']['id']
        if message['reply_to_message']['from']['id']:
            mute_id = message['reply_to_message']['from']['id']
            chat_id = message['chat']['id']
            username = message['message']['from']['first_name']
            return gen(mute_list, mute_id, muter, chat_id, username)


# deleting message
def del_message(chat_id, message_id):
    params = {'chat_id': chat_id,
              'message_id': message_id}
    return requests.get('deleteMessage', params)


# mute list redactor
# дописать таймер и оповещения к голосованию
def gen(mute_list, mute_id, muter, chat_id, username):
    if mute_id in mute_list:
        if muter in mute_list[mute_id]:
            methods.send_message(URL, chat_id, None, 'Already in list')
        else:
            mute_list[mute_id].append(muter)
            if len(mute_list[mute_id]) >= 3:
                restrict_user(chat_id, mute_id, timestamp(), False, False, False, False)
                methods.send_message(URL, chat_id, None, username + ' restricted')
                del mute_list[mute_id]
                print(mute_list)
            else:
                print(mute_list)
                votes = len(mute_list[mute_id])
                methods.send_message(URL, chat_id, None, str(3 - votes) + ' votes left')
    else:
        mute_list[mute_id] = [muter]
#        restrict_user(chat_id, mute_id, timer(), False, False, False, False)
        time.sleep(30)
        print(mute_list)
        votes = len(mute_list[mute_id])
        methods.send_message(URL, chat_id, None, str(3 - votes) + ' votes left')
