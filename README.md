# 🎓 Student Portfolio App — Flask + PostgreSQL + Docker

Добро пожаловать в **Student Portfolio App** — веб-приложение для управления индивидуальными достижениями студентов.  
Система создана с использованием **Flask**, **PostgreSQL** и **Docker** и предоставляет удобный интерфейс для студентов.
А именно выгрузку работ в разных видах, просмотр работ других студентов, а также возможность скачать резюме студента.

---

## 🚀 Быстрый запуск

Для запуска приложения на вашем компьютере потребуется установленный **Docker** и **Docker Compose**.

---

### 📦 Шаг 1. Клонируйте репозиторий

Откройте терминал и выполните:

```bash
git clone [https://github.com/ivan-suhonenkov5/KPresume]
cd your-repo-name
```
---

### ⚙️ Шаг 2. Создайте файл `.env`

Создайте в корневой директории файл `.env` и добавьте в него следующие строки:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://postgres:postgres@db:5432/student_portfolio
```

Вы можете задать свой `SECRET_KEY`.

---

### 🐳 Шаг 3. Соберите и запустите приложение

Просто выполните:

```bash
docker compose up --build
```

После завершения сборки приложение будет доступно по адресу:  
[http://localhost:5000](http://localhost:5000)

---

## 🧪 Основные команды Docker

| Команда                             | Описание                                   |
|-------------------------------------|--------------------------------------------|
| `docker compose up`                | Запустить проект                           |
| `docker compose down`              | Остановить и удалить контейнеры            |
| `docker compose build`             | Пересобрать образы                         |
| `docker compose logs -f`           | Логи в реальном времени                    |
| `docker exec -it app bash`         | Войти внутрь контейнера с Flask            |
| `docker exec -it db psql -U postgres` | Войти в PostgreSQL через CLI             |

---

## 📁 Структура проекта

```
├── app/                   # Основной код Flask-приложения
│   ├── templates/
│   ├── static/
│   ├── routes/
│   └── models/
├── .env                   # Переменные окружения
├── Dockerfile             # Сборка Flask-приложения
├── docker-compose.yml     # Конфигурация docker-compose
├── requirements.txt       # Python зависимости
├── config.py              # Настройки приложения
└── run.py                 # Точка входа Flask
```

---

## 📌 Используемые технологии

- 🔥 Flask
- 🐘 PostgreSQL
- 🐳 Docker & Docker Compose
- 🔐 Flask-Login, Flask-WTF, Flask-Bcrypt
- 📄 pdfkit + wkhtmltopdf
- 🖼 Pillow
- 📦 SQLAlchemy

---

