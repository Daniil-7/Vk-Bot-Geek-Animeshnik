# Импортируем библиотеку vk_api
import vk_api
import requests
from random import randint

# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType


token = "token"

# Подключаем токен и longpoll
bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)
upload = vk_api.VkUpload(bh)
session = requests.Session()


# Создадим функцию для ответа на сообщения в лс группы
def blasthack(id, text):
    bh.method("messages.send", {"user_id": id, "message": text, "random_id": 0})


# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        # Чтобы наш бот не слышал и не отвечал на самого себя
        if event.to_me:

            # Для того чтобы бот читал все с маленьких букв
            message = event.text.lower()
            # Получаем id пользователя
            id = event.user_id
            if message == "привет":
                blasthack(id, "Привет, я Гик!")
            elif message == "начать":
                blasthack(id, 'Напиши "тянка" чтобы получить картинку тянки.')
            elif message == "инструкция":
                blasthack(id, 'Напиши "тянка" чтобы получить картинку тянки.')
            elif message == "тянка":
                attachments = []
                image_url = (
                    "https://www.thiswaifudoesnotexist.net/example-"
                    + str(randint(0, 99999))
                    + ".jpg"
                )
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                attachments.append("photo{}_{}".format(photo["owner_id"], photo["id"]))
                give.messages.send(
                    user_id=id,
                    random_id=0,
                    attachment=",".join(attachments),
                    message="",
                )
            else:
                blasthack(
                    id,
                    'Я вас не понимаю! :( Напиши "тянка" чтобы получить картинку тянки.',
                )
