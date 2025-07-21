# 🛒 Django E-Commerce Web App

This is a fully functional and modern **e-commerce web application** built with **Django**, enhanced with:

- 🧠 **AI-powered product description generator**
- 💬 **Interactive ChatGPT-based support assistant**
- 🛍️ Features like: Add to Cart, Buy Now, Search, User Auth, Cart Tracking

---

## 🚀 Features

### 👤 User Account

- Signup/Login via **Email + Password**
- Session-based cart support
- Logout functionality

### 🛍️ Shopping & Cart

- Browse all products
- Add to cart & Buy Now functionality
- Dynamic cart icon with quantity
- Live search bar to filter products

### 💬 AI Chatbot (OpenAI-Powered)

- Integrated chatbot using **ChatGPT API**
- Users can ask questions, get order support, and more

### ✍️ AI Product Description Generator

- Admin or seller can generate smart product descriptions using GPT

---

## 📦 Tech Stack

| Technology      | Usage                    |
| --------------- | ------------------------ |
| Python / Django | Backend Framework        |
| HTML / CSS / JS | Frontend UI              |
| SQLite          | Default DB (can upgrade) |
| OpenAI API      | Chatbot + AI description |

---

## 💻 Local Setup Instructions

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ecommerce-project.git
cd ecommerce-project

# Set up a virtual environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Run server
python manage.py runserver
```


