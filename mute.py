mute_list = {}
mute_count = {}
mute_timer = {}


def delete_message(chat_id, message_id):
    params = {
        'chat_id': chat_id,
        'message_id': message_id
    }
    return request('deleteMessage', params)


def mute(chat_id, user_id, message):
    return delete_message(chat_id, user_id)


def message_checker(message, list):
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


# mute count
def counter(mute_list):
    if len(list(mute_list.keys())) = 3:
        print('DING DING DING')
















'''    id = user_id
    if id in mute_list:
        if mute_list[id][count] < 2:
            mute_list[id][count] += 1
        else:
            mute(chat_id, id)
    else:
        mute_list[id] = {'count': 1}
'''