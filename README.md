# 📚 E-Book Store

A **Django + Tailwind CSS** based web application for reading and managing digital books.  
Users can **sign up**, **sign in**, **browse books**, and **download e-books** with a clean, responsive interface.

---

## 🚀 Features

- 🔐 User Authentication (Sign In / Sign Up / Logout)  
- 📘 Browse and view e-books  
- 🔎 Search books by title or author  
- 📥 Download e-books (PDF format)  
- 🧑‍💼 Admin panel for managing books and users  
- 💻 Responsive UI built with **Tailwind CSS**  
- 🗂️ Database integration using **SQLite**

---

## 🛠️ Tech Stack

**Frontend:**  
- HTML  
- Tailwind CSS  
- JavaScript  

**Backend:**  
- Python  
- Django  

**Database:**  
- SQLite  

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally 👇

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/ebook-store.git
cd ebook-store

# 2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run database migrations
python manage.py migrate

# 5️⃣ Start the development server
python manage.py runserver

ebook-store/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── static/
│   ├── css/
│   ├── images/
│   │   └── Screenshot (81).png
│   └── js/
├── templates/
│   ├── base.html
│   ├── book_list.html
│   └── auth/
│       ├── login.html
│       └── signup.html
├── ebook/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── bookstore/
    ├── settings.py
    ├── urls.py
    └── wsgi.py


---

