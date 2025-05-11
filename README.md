# 📰 FinNews

A minimalist financial news aggregator built with Django, Celery, and Redis.  
Clean UI powered by [mini.css](https://minicss.org/), built for speed and simplicity.

---

## 🚀 Features

- ✅ Parse and display RSS/Atom feeds
- 🕒 Hourly automatic updates with Celery Beat
- 📦 Background task queue with Redis
- ✨ Minimalist UI (responsive and fast)
- 🧩 Django admin support for managing feeds

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/eddipa/finnews.git
cd finnews
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file (see `.env.example`):

```bash
cp .env.example .env
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

---

## ⏱ Running Celery

**Worker:**

```bash
celery -A finnews worker --loglevel=info
```

**Beat Scheduler (for periodic tasks):**

```bash
celery -A finnews beat --loglevel=info
```

---

## 🛠 Stack

- Python 3.x
- Django 5.x
- Celery 5.x
- Redis (broker)
- django-celery-beat
- mini.css (UI)

---

## 📄 License

MIT License © 2025
