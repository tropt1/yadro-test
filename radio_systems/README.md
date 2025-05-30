# Задачи от команды "Радиочастотные системы"

В этой папке находятся решения задач от команды YADRO "Радичастотные системы"

---

## 📋 Содержание
1. [Требования](#-требования)
2. [Установка](#-установка)
3. [Использование](#-использование)
4. [Docker](#-docker)

---

## 🛠 Требования
- Linux-система (или WSL для Windows)
- Docker (опционально, для задачи 4)
- Python 3.x (для запуска Python-скрипта)

---

## 📥 Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/tropt1/yandro-test.git
   cd yadro-test
   ```
2. Создайте файл config.txt (для задачи 3):
   ```bash
    echo -e "name: test_server\npath: /home/user/data\nfile: data.txt\nport: 8080\nlog path: /var/log/app" > config.txt
   ```

---

## 🚀 Использование

### 1. Запись строки в файл
   Команда:
   ```bash
   echo "Hello, DevOps!" | tee ~/hello.txt
   ```
   - Результат: Строка сохраняется в ~/hello.txt и выводится в терминал.

### 2. Поиск ошибок в логах
   Команда (пример для /var/log/syslog):

   ```bash
   grep -i 'error' /var/log/syslog | head -n 5
   ```

   - Замените error на искомое слово (например, warning).
   - Вывод: Первые 5 совпадений.

### 3. Поиск строк в файле
### Bash-скрипт
   ```bash
   ./search.sh config.txt path
   ```
   - Ищет слово path в файле config.txt.

### Python-скрипт
   ```bash
   python3 search.py config.txt path
   ```
   - Регистронезависимый поиск.

### 4. Docker
   Соберите оптимизированный образ:

   ```bash
   docker build -t devops-app .
   ```
   Запустите контейнер:
   ```bash
   docker run -it devops-app
   ```

## 🐳 Docker
### Особенности оптимизированного Dockerfile:
   - Объединение команд RUN для уменьшения слоев.
   - Очистка кэша APT.
   - Копирование всех файлов за один шаг.
