
# OUSL Book Distribution System BACKEND

Welcome to the **OUSL Book Distribution System**, a web application designed to efficiently manage and distribute books at the Open University of Sri Lanka (OUSL). This system includes both frontend and backend components, with this repository containing the **Django backend**.

Whether you’re a beginner or a professional, exploring this project will help you **enhance your knowledge and grow in your IT journey**.

This system leverages **Django’s internal signals** for efficient communication between components, follows a **loosely coupled architecture**, and is designed to be **microservice-ready**, making it flexible and scalable for future extensions.

---

## 🚀 Features

* Manage books, students, and distribution records
* User authentication for Admin and Staff
* REST API endpoints for frontend integration
* Admin dashboard for easy management
* Book reservation system for students
* Automated notifications (email/SMS)
* Request status tracking
* QR code scanning for books
* Feedback and issue reporting

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/OUSL-Book-Distribution-System-Django-Backend.git
```

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

5. **Configure the `.env` file**

Create a file named `.env` in the root directory of the project and add the following information:

```env
# Main Database
DATABASE_NAME="OUSLBookDB"
DATABASE_USER="root"
DATABASE_PASSWORD=""
DATABASE_HOST="127.0.0.1"
DATABASE_PORT="3306"

# Test Database
TEST_DATABASE_NAME="TestOUSLBookDB"

# Email settings
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
```

> **Note:**
>
> * Replace empty fields with your actual database and email credentials.
> * `.env` helps Django load your sensitive credentials securely.
> * For the email system, you can use Gmail or other SMTP providers.

6. **Run database migrations**

```bash
python manage.py migrate
```

7. **Create a superuser**

```bash
python manage.py createsuperuser
```

8. **Start the development server**

```bash
python manage.py runserver
```

* Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the application running.
* Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to access the admin panel.

---

## 🧩 Tech Stack

* **Backend:** Python, Django
* **Database:** MySQL (default), SQLite for testing
* **API:** Django REST Framework

---

## 🔹 New Unique Features

1. **Book Reservation** – Students can reserve books online, reducing queues.
2. **Automated Notifications** – Sends emails/SMS for issue confirmations, request approvals, and low stock alerts.
3. **Request Status Tracking** – Students can track requests as “Pending,” “Approved,” or “Ready for Collection.”
4. **QR Code Scanning for Books** – Staff can scan QR codes to check book details, update inventory, and record transactions instantly.
5. **Feedback & Issue Reporting** – Students and staff can report issues; admins can review and take action.

---

## 👨‍💻 Author

**Gangula Sandaru Dinusantha**
[GitHub Profile](https://github.com/yourusername)

---

## 💡 Final Note

I hope anyone who explores this project **enhances their knowledge** and grows in their **IT industry journey** by learning from my work. Keep experimenting, learning, and innovating.

**Happy coding! 😊**



 you want me to do that?
