# a) Базовый образ
FROM ubuntu:22.04

# b) Устанавливаем зависимости: python3, pip, requests
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      python3 python3-pip && \
    pip3 install requests && \
    rm -rf /var/lib/apt/lists/*

# c) Копируем скрипт
COPY ./section1/http_checker.py /app/http_checker.py
WORKDIR /app

# Сделать скрипт исполняемым
RUN chmod +x http_checker.py

# d) При старте контейнера запускаем скрипт
ENTRYPOINT ["python3", "http_checker.py"]
