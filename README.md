## Краткий обзор

В этом репозитории собраны два независимых тестовых задания для стажировки в YADRO:

- Telecom‑проект (telekom_project) 🚀
- Radio Systems (radio_systems) 🎯

Языки и технологии: Python (58.5 %), Dockerfile (34.5 %), Shell (7 %).

## Структура репозитория 📂 

.
├── telekom_project       # Задание для Telecom‑команды
│   ├── section1          # Part 1: HTTP‑чекер на Python
│   │   ├── http_checker.py
│   │   └── requirements.txt
│   ├── section2          # Part 2: Docker‑образ для запуска чекера
│   │   └── Dockerfile
│   └── section3          # Part 3: Ansible‑playbook для автоматизации
│       ├── inventory.ini
│       └── playbook.yml
└── radio_systems         # Задание для Radio Systems

## Требования 🔧

- Git 📜
- Python 3.8+ и библиотека «requests» 🐍
- Docker (для проверки section2) 🐳
- Ansible 2.9+ и коллекция «community.docker» 🤖
