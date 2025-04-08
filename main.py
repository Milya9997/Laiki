import json
import time
import requests
from flask import Flask, request

app = Flask(__name__)

# Загружаем обязательные ссылки из config.json
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

REQUIRED_LINKS = config.get("required_links", [])

# Словарь для хранения данных пользователей
user_states = {}

# Проверка лайков (псевдореализация — реальную надо через VK API)
def has_liked_required_links(user_id):
    # Заглушка — всегда возвращаем True
    # Здесь можно подключить VK API, чтобы реально проверять лайки
    return True

@app.route('/', methods=['POST'])
def handle():
    data = request.json
    user_id = str(data['user_id'])
    message = data['message']

    # Если пользователь отправил ссылку раньше времени
    if message.startswith("https://vk.com/"):
        if user_id not in user_states or not user_states[user_id]['approved']:
            return {
                "message": "Сначала поставьте лайки на обязательные посты. После этого вернитесь и отправьте свою ссылку."
            }

        # Всё в порядке, пользователь одобрен
        return {
            "message": "Ваша ссылка принята! Спасибо!"
        }

    # Если пользователь пишет команду для начала
    if message.lower() == "старт":
        user_states[user_id] = {"approved": False}
        links_text = "\n".join(REQUIRED_LINKS)
        return {
            "message": f"Поставьте лайки на следующие посты:\n{links_text}\n\nКогда закончите — отправьте 'Готово'."
        }

    # Если пользователь пишет "Готово"
    if message.lower() == "готово":
        if has_liked_required_links(user_id):
            user_states[user_id]['approved'] = True
            return {
                "message": "Проверка пройдена! Теперь отправьте свою ссылку на пост."
            }
        else:
            return {
                "message": "Вы не поставили лайки на все обязательные посты. Попробуйте ещё раз."
            }

    return {"message": "Напишите 'старт', чтобы начать."}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
