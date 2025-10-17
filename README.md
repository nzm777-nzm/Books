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

📷 Screenshot
🖼️ Book List Page
<img width="1366" height="768" alt="Screenshot (81)" src="https://github.com/user-attachments/assets/77b105e4-2fff-4a43-86ba-9f94089ad00d" />



---

✅ **How to make the image visible on GitHub:**
1. Move your image to this folder:  
   `static/images/Screenshot (81).png`
2. Commit & push both `README.md` and your image to GitHub.  
   GitHub will automatically render the image inside your README.  

Would you like me to make the README include a **“Login & Signup Page” screenshot** section too (you can add one later)?
