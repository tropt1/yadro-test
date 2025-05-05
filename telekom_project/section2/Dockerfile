FROM ubuntu:22.04

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y python3 python3-pip python-is-python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем скрипт
WORKDIR /app
COPY ./section1/http_checker.py ./section1/requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем скрипт
CMD ["python", "http_checker.py"]
