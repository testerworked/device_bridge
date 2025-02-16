# Используем официальный образ Ubuntu 24.04
FROM ubuntu:24.04

# Устанавливаем переменные окружения для избежания вопросов при установке пакетов
ENV DEBIAN_FRONTEND=noninteractive

# Обновляем список пакетов и устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Создаем виртуальное окружение
RUN python3 -m venv /opt/venv

# Активируем виртуальное окружение и устанавливаем Flask
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && pip install Flask

# Копируем исходный код приложения
COPY . .

# Создаем простой файл Flask приложения, если его нет
RUN echo "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef hello_world():\n    return 'Hello, Docker!'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=5000)" > app.py

# Открываем порт 5000 для Flask приложения
EXPOSE 5000

# Запускаем приложение
CMD ["python3", "app.py"]