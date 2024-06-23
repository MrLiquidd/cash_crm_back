# Используем официальный образ Python в качестве базового
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN apt update
RUN apt upgrade
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Открываем порт 8000 для доступа к серверу
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

