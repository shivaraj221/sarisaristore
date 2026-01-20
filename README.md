# 🏪 SariSari Store – Django Web Application

A full-stack Django web application designed for managing a Sari-Sari store. The project includes backend logic, frontend templates, static assets, custom Django commands, background tasks, and production-ready deployment configuration.

---

## 📋 Table of Contents

| Section | Description |
|---------|-------------|
| [Project Overview](#-project-overview) | Brief introduction to the application |
| [Features](#-features) | Key functionalities |
| [Technology Stack](#-technology-stack) | Tools and technologies used |
| [Project Structure](#-project-structure) | Complete folder and file layout |
| [Folder & File Explanation](#-folder--file-explanation) | Detailed explanation of each component |
| [Application Architecture](#-application-architecture) | System design overview |
| [Request Flow](#-request-flow) | How requests are processed |
| [Installation & Setup](#-installation--setup) | Local development setup |
| [Environment Configuration](#-environment-configuration) | Environment variables setup |
| [Database & Migrations](#-database--migrations) | Database configuration |
| [Admin Management](#-admin-management) | Django admin setup |
| [Static Files](#-static-files) | CSS, JS, and image handling |
| [Templates](#-templates) | HTML template structure |
| [Custom Commands](#-custom-commands) | Django management commands |
| [Background Tasks](#-background-tasks) | Asynchronous task processing |
| [Deployment (Render)](#-deployment-render) | Production deployment guide |
| [Security Guidelines](#-security-guidelines) | Security best practices |
| [Future Improvements](#-future-improvements) | Planned features |
| [License](#-license) | Licensing information |

---

## 🎯 Project Overview

This application is built using Django and follows a clean modular architecture.

It demonstrates:
- ✅ Separation of project and app structure
- ✅ Template-based frontend rendering
- ✅ Static file management
- ✅ Background task execution
- ✅ Custom Django management commands
- ✅ Production deployment using Render

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 👥 **User Management** | User registration and login system |
| 🛒 **Store Interface** | Complete store page with product management |
| ⚙️ **Admin Dashboard** | Django admin interface for store management |
| 🏗️ **Modular Backend** | Clean, organized backend structure |
| 🔧 **Custom Commands** | Django management commands for admin tasks |
| ⚡ **Background Tasks** | Asynchronous task processing support |
| 🚀 **Production Ready** | Ready-to-deploy configuration for Render |

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| **Backend Framework** | Django (Python) |
| **Frontend** | HTML, CSS, JavaScript |
| **Database (Dev)** | SQLite |
| **Database (Prod)** | PostgreSQL |
| **WSGI Server** | Gunicorn |
| **Deployment** | Render |
| **Version Control** | Git |
| **Task Queue** | Django Background Tasks |

---

## 📁 Project Structure

```
sarisari_store/
├── 📁 sarisari_store/          # Main project directory
│   ├── 📁 __pycache__/
│   ├── 📄 __init__.py
│   ├── 📄 asgi.py
│   ├── 📄 settings.py          # Project settings
│   ├── 📄 urls.py              # Main URL routing
│   └── 📄 wsgi.py
│
├── 📁 store/                   # Main Django app
│   ├── 📁 __pycache__/
│   ├── 📁 migrations/
│   ├── 📁 static/
│   │   └── 📁 store/          # CSS, JS, images
│   ├── 📁 templates/
│   │   └── 📁 store/          # HTML templates
│   ├── 📄 __init__.py
│   ├── 📄 admin.py            # Admin configuration
│   ├── 📄 apps.py
│   ├── 📄 models.py           # Database models
│   ├── 📄 tasks.py            # Background tasks
│   ├── 📄 tests.py
│   ├── 📄 urls.py             # App URL routing
│   └── 📄 views.py            # View logic
│
├── 📁 utils/                   # Utility functions
│   └── 📄 helpers.py
│
├── 📁 scripts/                 # Custom scripts
│   └── 📄 create_admin.py
│
├── 📁 manage.py                # Django management
├── 📄 requirements.txt         # Python dependencies
├── 📄 runtime.txt              # Python runtime version
├── 📄 Procfile                 # Render deployment config
├── 📄 build.sh                 # Build script
├── 📄 .env.example             # Environment template
├── 📄 .gitignore               # Git ignore rules
└── 📄 README.md                # This documentation
```

---

## 📄 Folder & File Explanation

| File/Folder | Purpose |
|-------------|---------|
| **sarisari_store/** | Main Django project directory |
| **store/** | Main application directory |
| **store/static/** | CSS, JavaScript, images |
| **store/templates/** | HTML templates |
| **store/migrations/** | Database migration files |
| **store/models.py** | Database models definition |
| **store/views.py** | Request handling logic |
| **store/urls.py** | URL routing for the app |
| **store/admin.py** | Django admin configuration |
| **store/tasks.py** | Background task definitions |
| **utils/** | Helper functions and utilities |
| **scripts/** | Custom Python scripts |
| **requirements.txt** | Python package dependencies |
| **Procfile** | Render process configuration |
| **build.sh** | Build script for deployment |
| **.env.example** | Environment variables template |

---

## 🏗️ Application Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│                    (HTML/CSS/JS)                        │
└───────────────┬─────────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────────────────┐
│                    Django Views                          │
│              (Business Logic Layer)                      │
└───────────────┬─────────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────────────────┐
│                  Django Models                           │
│              (Database Interaction)                      │
└───────────────┬─────────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────────────────┐
│                     Database                             │
│               (SQLite/PostgreSQL)                       │
└─────────────────────────────────────────────────────────┘
```

---

## 🔄 Request Flow

```
1. User Request → 2. URL Routing → 3. View Processing → 4. Database Query
       ↓               ↓                 ↓                 ↓
    Browser        urls.py            views.py         models.py
       ↓               ↓                 ↓                 ↓
8. Response ← 7. Template Render ← 6. Data Processing ← 5. Query Results
```

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/sarisari-store.git
cd sarisari-store
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Admin User
```bash
python manage.py createsuperuser
# OR use custom script
python scripts/create_admin.py
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```
Access at: `http://localhost:8000`

---

## 🔧 Environment Configuration

Create `.env` file with:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=sarisari_store
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Production Settings
PRODUCTION=False
```

---

## 🗄️ Database & Migrations

| Command | Description |
|---------|-------------|
| `makemigrations` | Create new migrations |
| `migrate` | Apply migrations to database |
| `showmigrations` | List all migrations |
| `sqlmigrate` | Show SQL for migration |
| `dbshell` | Open database shell |

**Reset Database:**
```bash
# Delete database
rm db.sqlite3

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
```

---

## 👑 Admin Management

### Default Admin
```bash
python manage.py createsuperuser
```

### Custom Admin Command
```bash
python scripts/create_admin.py
```

### Admin URL
```
http://localhost:8000/admin/
```

---

## 🎨 Static Files

| Type | Location | Description |
|------|----------|-------------|
| CSS | `store/static/store/css/` | Stylesheets |
| JS | `store/static/store/js/` | JavaScript files |
| Images | `store/static/store/images/` | Product images, icons |

**Collect Static Files (Production):**
```bash
python manage.py collectstatic
```

---

## 📝 Templates

| Template | Purpose |
|----------|---------|
| `base.html` | Base template with layout |
| `index.html` | Home page |
| `store.html` | Main store interface |
| `login.html` | User login page |
| `register.html` | User registration page |

---

## ⚙️ Custom Commands

### Create Admin Script
```python
# scripts/create_admin.py
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.create_superuser(
    username='admin',
    email='admin@sarisari.com',
    password='admin123'
)
```

Run with:
```bash
python scripts/create_admin.py
```

---

## ⚡ Background Tasks

### Task Definition
```python
# store/tasks.py
from background_task import background

@background(schedule=60)
def process_order(order_id):
    # Process order logic
    pass
```

### Run Task Worker
```bash
python manage.py process_tasks
```

---

## 🚀 Deployment (Render)

### 1. Connect Repository
- Connect your GitHub repository to Render

### 2. Configure Environment
| Variable | Value |
|----------|-------|
| `SECRET_KEY` | Random secret key |
| `DEBUG` | False |
| `ALLOWED_HOSTS` | your-app.onrender.com |
| `DATABASE_URL` | Postgres URL from Render |

### 3. Build & Deploy
Render will automatically:
- Install dependencies from `requirements.txt`
- Run `build.sh`
- Apply migrations
- Collect static files
- Start Gunicorn server

### 4. Manual Deployment
```bash
# Build
./build.sh

# Start server
gunicorn sarisari_store.wsgi:application
```

---

## 🔒 Security Guidelines

| Security Measure | Implementation |
|-----------------|----------------|
| **Secret Key** | Use environment variable |
| **Debug Mode** | Disable in production |
| **HTTPS** | Enable SSL in production |
| **CSRF Protection** | Enabled by default |
| **XSS Protection** | Django templates escape HTML |
| **SQL Injection** | Use Django ORM queries |
| **Password Hashing** | Django's PBKDF2 by default |

---

## 🔮 Future Improvements

| Feature | Priority | Status |
|---------|----------|--------|
| Inventory Management | 🔴 High | Planned |
| Sales Reporting | 🟡 Medium | Planned |
| Customer Accounts | 🟡 Medium | Planned |
| Barcode Scanning | 🔵 Low | Future |
| Mobile App | 🔵 Low | Future |
| Payment Integration | 🟡 Medium | Planned |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ **Support the Project**

If you find this project useful, please give it a star!

[![GitHub stars](https://img.shields.io/github/stars/yourusername/sarisari-store?style=social)](https://github.com/yourusername/sarisari-store)

**Happy Coding!** 🚀

</div>
