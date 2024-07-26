# Используем официальный образ Python
FROM python:3.11.5-slim

# Устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы проекта в рабочую директорию
COPY . /app
WORKDIR /app



# Run the application
CMD ["python", "bot.py"]