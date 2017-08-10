import methods
import mute
import parcer
import re
import teltoken
import time

URL = "https://api.telegram.org/bot" + teltoken.TOKEN + '/'
LIMIT = 10
TIMEOUT = 10


if __name__ == '__main__':

    methods.ping(URL)

    update_id = 0
    mute_id = {}
    mute_list = {}

    while True:
        upd = methods.make_request(URL, 'getUpdates', params={
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
                methods.log(username, text)
                print(chat_id, username, user_id, text)

                if 'gimme' in text:

                    search_pattern = re.compile('\\\\\w+')
                    keyword = search_pattern.search(text)

                    if keyword:
                        try:
                            link = parcer.link_modifier(keyword.group())
                            methods.send_message(URL, chat_id, message_id,
                                                 parcer.picture(link))
                        except ValueError:
                            methods.send_message(URL, chat_id, message_id,
                                                 'Not found ¯\\_(ツ)_/¯')
                    else:
                        methods.send_message(URL, chat_id, message_id,
                                             'Add "\\" before keyword')

#                if user_id in mute.mute_list:
#                    delete_message(chat_id, message_id)
#
#                if 'mute' in text:
#                    mute_id = i['message']['reply_to_message']['from']['id']
#                    mute.checker(chat_id, mute_id)

            except KeyError:
                print('Sticker')
                pass

        if len(upd) > 0:
            update_id = int(upd[-1]["update_id"])
