# Recommend-TG-bot

EN: Content- based Movie Recommendation telegram bot, based on Bert embeddings for genres, directors, actors and keywords from Movielens and TMDB datasets

RU:  Проект представляет из себя систему рекомендаций на основе содержания, интегрированную в телеграмм бота.
Рекомендации основаны эмбеддингах жанров, актёров, режиссеров и ключевых слов, полученных из BERT. Размерность эмбеддингов понижается с помощью UMAP и SVD, а затем строятся кластеры. 
Поиск происходит похожих фильмов происходит с помощью Laplasian Kernel.

## Структура проекта

- `Dockerfile`: Файл Dockerfile для создания Docker-образа проекта.
- `__pycache__/`: Каталог с скомпилированными файлами Python.
- `bot.py`: Основной файл с кодом бота.
- `data.py`: Файл с функциями для обработки данных.
- `rec_data.csv`: CSV-файл с данными для рекомендаций.
- `requirements.txt`: Файл с зависимостями Python.
- `notebooks`: папка с ipynb файлами, в которых реализованы EDA, получение эмбеддингов, понижение размерности, кластеризация и получение схожих фильмов на основе Лапласового ядра


## Установка и запуск

1. Установите Docker, если его еще нет.
2. Скачайте образ проекта из DockerHub
3. Зайдите в телеграм и найдите бота https://t.me/Kino_rec_bot
   
Образ:
```bash
docker pull bogdan01m/recommend-tg-bot:1.0
```
Запуск:
```bash
docker run -d bogdan01m/recommend-tg-bot:1.0
```


