# 🚀 CI/CD Demo Website

Flask asosidagi oddiy veb-sayt, **GitHub Actions** orqali avtomatik deploy qilinadi.

![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![Docker](https://img.shields.io/badge/Docker-29.1.3-blue)

## 🛠️ Texnologiyalar

- **Flask** — veb-framework
- **Docker** — konteynerizatsiya
- **GitHub Actions** — CI/CD
- **Gunicorn** — production server
- **Pytest** — testlar

## 📦 Ishga tushirish

### Lokal

    pip install -r requirements.txt
    python src/app.py

Sayt: http://localhost:5000

### Docker bilan

    docker build -t my-website:v1 .
    docker run -d -p 5000:5000 my-website:v1

## 🧪 Testlar

    pytest tests/ -v

**Natija:** 3 ta test ✅

## 🔄 CI/CD

Har bir `main` branch ga push qilinganda:

1. ✅ Testlar bajariladi
2. 🐳 Docker image quriladi
3. 📤 Docker Hub ga push qilinadi
4. 🚀 Serverga deploy qilinadi

## 🌐 URL

- Bosh sahifa: http://localhost:5000
- Health: http://localhost:5000/health

## 📁 Loyiha tuzilishi

    my-website/
    ├── .github/workflows/     # CI/CD konfiguratsiya
    ├── src/
    │   ├── app.py            # Asosiy Flask kodi
    │   └── templates/
    │       └── index.html    # HTML shablon
    ├── tests/
    │   └── test_app.py       # Testlar
    ├── Dockerfile            # Docker konfiguratsiya
    ├── requirements.txt      # Kutubxonalar
    └── README.md

## 📝 Litsenziya

MIT
