# 🍲 recepiebook_django

A **Django 5.x** web application for showcasing recipes with Bootstrap styling and multiple pages (landing, about, contact, recipes).

---

## 🧩 Project Overview

`recepiebook_django` is a Django project that allows users to:

- Browse recipes with images  
- View recipe details in a clean, Bootstrap-styled layout  
- Access static pages like About and Contact  
- Submit messages via a Contact form with basic validation and flash messages  

**Apps & Templates:**

- **Apps:** `home`, `veg`  
- **Templates:**  
  - `base.html` – navbar (Home, Recipes, About, Contact)  
  - `index.html` – landing page with hero and feature sections  
  - `about.html` – static information page  
  - `contact.html` – contact form with POST handling  
- **Media:** Images stored under `media/recepie_images/` (ensure images are added locally for display)

---

## 🛠️ Features

- Landing page with hero/feature sections  
- Recipes page with images and descriptions  
- About page with static content  
- Contact page with form validation, success messages, and redirect after submission  
- Bootstrap-based responsive UI  

---

## 🚀 Tech Stack

- **Backend:** Django 5.x (Python)  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Database:** SQLite  
- **Media:** Images under `media/recepie_images/`  

---

## 📁 Project Structure

recepiebook_django/
├── home/ # Main app (views, templates, static)
├── veg/ # Secondary app (optional)
├── mysite/ # Django project settings
├── media/recepie_images/ # Uploaded recipe images
├── manage.py # Django entry point
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 💡 Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/B-chand/recepiebook_django.git
cd recepiebook_django
Create a virtual environment

python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Apply migrations

python manage.py migrate
Create superuser (optional, for admin access)

python manage.py createsuperuser
Start the development server

python manage.py runserver
Open in browser

http://127.0.0.1:8000/
🖼️ Usage
Visit Home for landing page and featured recipes

Recipes page displays images and details

About page shows static information

Contact page allows submitting messages with success flash messages

Add images to media/recepie_images/ to display in the templates

📌 Contributing
Fork the repository

Create a new branch

Make edits and commit

Open a pull request

