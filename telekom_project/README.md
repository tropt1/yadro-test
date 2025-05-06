# Тестовое задание для Телеком команды 🚀

## Описание

Данный репозиторий содержит по‑шаговую реализацию тестового задания:

1. **Part 1**: Python‑скрипт отправляет 5 разных HTTP‑запросов к сервису https://httpstat.us, логирует ответы для кодов 1xx–3xx и генерирует исключения для кодов 4xx–5xx. 🐍  
2. **Part 2**: Dockerfile на базе Ubuntu 22.04 собирает образ, устанавливает зависимости и запускает скрипт при старте контейнера. 🐳  
3. **Part 3**: Ansible‑playbook автоматизирует установку Docker на хосте, сборку образа, запуск контейнера и проверку работы скрипта через логи. 🤖

Проект хранит все изменения в ветке **master**, каждый раздел зафиксирован отдельным коммитом. 📦

---

## Структура репозитория 📂

```
.
├── section1
│   └── http_checker.py         # Скрипт для HTTP‑запросов 📝
├── section2
│   └── Dockerfile              # Сборка образа на Ubuntu 22.04 🐳
├── section3
│   ├── inventory.ini           # Инвентори для Ansible (localhost) 📋
│   └── playbook.yml            # Playbook для установки Docker и проверки скрипта 🎯
└── README.md                   # README файл 📋
```

---

## Требования 📋

- Git  
- Docker (для локальной проверки раздела 2)  
- Ansible 2.9+ и коллекция `community.docker`  
- Python 3.8+ и библиотека `requests` 🐍  

---

## Запуск ▶️

### Part 1. Скрипт 🐍

1. Убедитесь, что установлен Python 3 и модуль `requests`:
   ```bash
   python3 -m pip install requests
   ```
2. Сделайте скрипт исполняемым и запустите:
   ```bash
   chmod +x section1/http_checker.py
   python3 section1/http_checker.py
   ```

### Part 2. Docker 🐳

1. Собрать образ:
   ```bash
   docker build -t http_checker:latest -f section2/Dockerfile .
   ```
2. Запустить контейнер и просмотреть логи:
   ```bash
   docker run --rm  http_checker:latest
   docker logs httpstat
   ```

### Part 3. Ansible 🤖

1. Установите коллекцию `community.docker`:
   ```bash
   ansible-galaxy collection install community.docker
   ```
2. Перейдите в каталог `ansible` и запустите playbook:
   ```bash
   cd section3
   ansible-playbook -i inventory.ini playbook.yml
   ```
3. В выводе вы увидите:
   - результат установки Docker ✔️  
   - сборку и запуск контейнера ✔️  
   - логи выполнения скрипта 📜    
