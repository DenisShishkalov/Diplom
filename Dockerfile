# Используем официальный slim-образ Python 3.9
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей в контейнер
COPY requirements.txt ./

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения в контейнер
COPY . .

# Определяем переменные окружения
ENV SECRET_KEY="SECRET_KEY"

# Создаем директорию для медиафайлов
RUN mkdir -p /materials/media

# Пробрасываем порт, который будет использовать Django
EXPOSE 8000

# Команда для запуска приложения
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ['sh', '-c', 'python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000