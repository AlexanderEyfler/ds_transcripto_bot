# Transcripto Telegram bot

This bot was created during the Elbrus DataScience training program for initial acquaintance with Docker and logging in Python

Instructions for running a bot using Docker (in Russian):

1. Форкинте репозиторий и скопируйте форк `git clone` себе на устройство

2. В **Dockerfile**, для работы бота нужно указать валидный

токен Телеграм-бота в поле 
```
ENV TOKEN='вот_прямо_сюда_скопировать'
```

3. Создайте **docker image** из отредактированного **Dockerfile**, введя команду:
```

docker build . -t type_image_name_here

```

4. Убедитесь, что **docker image** создан корректно, вы должны видеть свой образ по команде 
```
docker images
```

5. Запустите контейнер на основе вашего образа в фоновом **detached mode** режиме с помощью команды
```
docker run -d -p 80:80 type_image_id_here
```

6. Убедиться, что контейнер успешно запущен и работает можно по команде

```
docker ps -a
```

7. **Поздравляю! Вы восхитительны!** Телеграм-бот успешно работает!