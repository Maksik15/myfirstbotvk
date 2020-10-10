from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import time

token ='303c26196615bb78102e2e792e2486f391ce3f87f5ea8f7f128d85cf2a0ee33e1e56103435de408ab07f9'
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def sender(id, text):
    vk_session.method("messages.send", {"peer_id": id, "message": text, "random_id":0})

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения:'+ str(event.text))
            if event.to_me:

                msg = event.text.lower()
                id = event.user_id

                if msg == 'привет':
                    sender(id, 'Добрый вечер!')
                elif msg == 'пока':
                    sender(id,'До встречи')

time.sleep(1)





  