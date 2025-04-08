VK Like Bot на Render

1. Отредактируйте config.json, установив:
   - group_token: токен вашей группы из ВК.
   - user_token: токен пользователя для проверки лайков.
   - confirmation_code: confirmation code из Callback API ВКонтакте.
   - required_links: список обязательных ссылок на посты.
2. Загрузите файлы в репозиторий GitHub.
3. Создайте новый Web Service на Render, подключив ваш репозиторий.
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py
4. Настройте Callback API в вашей группе ВК с URL, предоставленным Render.
5. Бот будет работать 24/7.
