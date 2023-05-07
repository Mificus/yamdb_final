![Yamdb_final](https://github.com/Mificus/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Продолжение команндного проекта. 

В проекте реализуем: 
 * автоматический запуск тестов,
 * обновление образов на Docker Hub,
 * автоматический деплой на боевой сервер при пуше в главную ветку main.

Полная документация по ссылке:
http://51.250.99.216/redoc

## Установка
Склонировать проект https://github.com/Mificus/yamdb_final.git

* Выполнить вход на удаленный сервер (например,  Yandex.Cloud).
* Развернуть виртуальную машину
* Остановить nginx на ВМ
```angular2html
sudo systemctl stop nginx
```
* Установить докер sudo apt install docker.io
* Установить последнюю версию docker-compose
```angular2html
curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```
* Скопировать файлы docker-compose.yaml и nginx/default.conf из вашего проекта 
на сервер в home/<ваш_username>/docker-compose.yaml и 
home/<ваш_username>/nginx/default.conf соответственно. Командой scp
* Прописать все секреты на гитхабе
* Собираем файлы статики, Запускаем миграции и создаём суперюзера
```angular2html
sudo docker-compose exec web python3 manage.py makemigrations
sudo docker-compose exec web python3 manage.py migrate
sudo docker-compose exec web python3 manage.py collectstatic --no-input
sudo docker-compose exec web python3 manage.py createsuperuser
```

#### Дополнительная инструкция для файла redoc
1. На сервере прописываем команды 
```angular2html
sudo docker exec -it  idконтейнер bash 
```
idконтейнер - ввести id контейнера web
Попадаем внуть этого контейнера
2. ls ищем папку static
3. Создаём файл redoc
```
touch static/redoc.yaml
```
4. Устанавливаем nano и открываем его
```angular2html
apt-get update
apt-get install nano
nano redoc.yaml
```
5. Копируем всё из файла redoc.yaml на компьютере в файл на сервере

#### Автор
Ласточкин Максим