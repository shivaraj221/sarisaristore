# **🏪 Sari-Sari Store Management System**

A full-stack Django web application for managing a Sari-Sari store with customer feedback capabilities.

---

## **📋 Table of Contents**

- Overview  
- Features  
- Technology Stack  
- Project Structure  
- Installation & Setup  
- Usage  
- Deployment  
- License

---

## **📖 Overview**

A complete Sari-Sari Store management system where:
- Store owner manages products
- Customers register and login
- Customers view all store products
- Customers submit feedback
- All feedbacks are displayed with JavaScript
- Admin manages everything via dashboard

---

## **✨ Features**

**Store Management:**
- ✅ Product catalog management
- ✅ Customer registration system
- ✅ Customer login system
- ✅ Store interface display

**Customer Features:**
- ✅ View all store products
- ✅ Submit product feedback
- ✅ See all feedbacks dynamically with JavaScript

**Admin Features:**
- ✅ Django admin dashboard
- ✅ View registered customers
- ✅ Monitor all feedbacks
- ✅ AI sentiment analysis on feedbacks

**Technical Features:**
- ✅ Background task processing
- ✅ Custom admin creation command
- ✅ Ready for Render deployment

---

## **🛠️ Technology Stack**

**Backend:** Django (Python)  
**Frontend:** HTML, CSS, JavaScript  
**Database:** SQLite (Development), PostgreSQL (Production)  
**Server:** Gunicorn  
**Deployment:** Render  
**Version Control:** Git

---

## **📁 Project Structure**

```
sarisaristore-main/
│   manage.py
│   requirements.txt
│   Procfile
│   render.yaml
│
├───core/                     # Main store application
│   │   models.py            # Database models (Products, Customers, Feedback)
│   │   views.py             # Business logic
│   │   admin.py             # Admin interface
│   │   tasks.py             # Background tasks
│   │   utils.py             # Utility functions
│   │   debug.py             # Debug tools
│   │   serializers.py       # API serializers
│   │   urls.py              # App URLs
│   │
│   ├───management/commands/
│   │       create_admin.py  # Custom admin command
│   │
│   └───migrations/         # Database migrations
│
├───main/                   # Project settings
│       settings.py
│       urls.py
│       wsgi.py
│       asgi.py
│
├───static/                # Frontend assets
│       app.js            # JavaScript for store and feedback display
│       style.css         # Store styling
│
└───templates/            # HTML pages
        index.html        # Store homepage
        login.html        # Customer login
        register.html     # Customer registration
        store.html        # Products display & feedback
```

---

## **⚙️ Installation & Setup**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Apply migrations
python manage.py migrate

# 3. Create store admin
python manage.py create_admin

# 4. Run server
python manage.py runserver
```

Visit: http://localhost:8000

---

## **🎯 How It Works**

1. **Store Setup** → Admin adds products to catalog
2. **Customer Registration** → Customers sign up via `register.html`
3. **Customer Login** → Customers login via `login.html`  
4. **View Store** → Customers see all products in `store.html`
5. **Submit Feedback** → Customers submit feedback on products
6. **View Feedbacks** → JavaScript in `app.js` shows all feedbacks dynamically
7. **Admin Management** → Store owner manages everything at `/admin`

---

## **🚀 Deployment to Render**

1. Push code to GitHub
2. Create Web Service on Render
3. Connect repository
4. Add environment variables:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `DATABASE_URL`

Configuration files included: `Procfile`, `render.yaml`, `runtime.txt`

---

## **📝 License**

MIT License

---

**Your Sari-Sari Store management system is ready!** 🏪
