import methods
import mute
import re
import requests
import parcer
import teltoken

URL = "https://api.telegram.org/bot" + teltoken.TOKEN + '/'
LIMIT = 10
TIMEOUT = 10


def delete_message(chat_id, message_id):
    params = {
        'chat_id': chat_id,
        'message_id': message_id
    }
    return make_request('deleteMessage', params)


if __name__ == '__main__':

    ping()

    update_id = 0
    mute_id = {}
    list = {}

    while True:
        upd = make_request('getUpdates', params={
            'limit': LIMIT,
            'timeout': TIMEOUT,
            'offset': update_id + 1})

        for i in upd:
            try:
                message = i['message']
                chat_id = i['message']['chat']['id']
                message_id = i['message']['message_id']
                user_id = i['message']['from']['id']
                username = i['message']['from']['first_name']
                text = i['message']['text'].lower()
                log(text)
                print(chat_id, username, user_id, text)

                if 'gimme' in text:

                    search_pattern = re.compile('\\\\\w+')
                    keyword = search_pattern.search(text)

                    if keyword:
                        try:
                            link = parcer.link_modifier(keyword.group())
                            send_message(chat_id, message_id,
                                         parcer.picture(link))
                        except ValueError:
                            send_message(chat_id, message_id,
                                         'Not found ¯\\_(ツ)_/¯')
                    else:
                        send_message(chat_id, message_id,
                                     'Add "\\" before keyword')

#                if user_id in mute.mute_list:
#                    delete_message(chat_id, message_id)
#
#                if 'mute' in text:
#                    mute_id = i['message']['reply_to_message']['from']['id']
#                    mute.checker(chat_id, mute_id)

                list = mute.message_checker(message, list)
                print(list)
            except KeyError:
                print('Sticker')
                pass

        if len(upd) > 0:
            update_id = int(upd[-1]["update_id"])
