

````markdown
# OUSL Book Distribution System

This is the **OUSL Book Distribution System**, a web application designed to manage and distribute books efficiently for the Open University of Sri Lanka (OUSL). The system includes both frontend and backend components, with this repository containing the **Django backend**.

---

## 🚀 Features

- Manage books, students, and distribution records  
- User authentication (Admin and Staff)  
- REST API endpoints for integration with frontend  
- Database management with SQLite (default)  
- Admin dashboard for easy management  

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/OUSL-Book-Distribution-System-Django-Backend.git
````

2. **Go to the project directory**

```bash
cd OUSL-Book-Distribution-System-Django-Backend
```

3. **Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run database migrations**

```bash
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Start the development server**

```bash
python manage.py runserver
```

Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** to see the application running.
Visit **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)** to access the admin panel.

---

## 🧩 Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite (default)
* **API:** Django REST Framework (if applicable)

---

## 👨‍💻 Author

**Gangula Sandaru Dinusantha**
[GitHub Profile](https://github.com/yourusername)

---


happy coding...................................:)

