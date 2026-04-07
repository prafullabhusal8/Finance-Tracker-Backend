# 💰 Finance Tracker System (Flask Backend + Templates)

## 📌 Project Overview

This project is a **Python-based Finance Tracking System** built using Flask. It allows users to manage their financial records such as income and expenses, view transaction history, and analyze financial summaries.

The system follows a clean backend architecture with proper validation, error handling, and a simple frontend interface using HTML templates.

---

## 🚀 Features

### 🔹 Transaction Management

* Add new transactions (Income / Expense)
* View all transactions
* Update and delete transactions (API level)
* Each transaction includes:

  * Amount
  * Type (Income / Expense)
  * Category
  * Date
  * Notes (optional)

---

### 🔹 Financial Summary

* Total Income calculation
* Total Expense calculation
* Current Balance
* Real-time updates based on stored data

---

### 🔹 Validation & Error Handling

* Prevents negative transaction values
* Ensures required fields are filled
* Displays error messages on frontend
* Handles invalid input safely

---

### 🔹 Backend + Frontend Integration

* REST API endpoints for backend operations
* HTML templates (Jinja2) for user interface
* Form-based data entry with validation feedback

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Frontend:** HTML, Jinja Templates
* **Tools:** VS Code, Git, GitHub

---

## 📂 Project Structure

```
finance-system/
│
├── app.py
├── models.py
│
├── routes/
│   ├── api_routes.py
│   └── web_routes.py
│
├── services/
│   └── summary_service.py
│
├── utils/
│   └── validators.py
│
├── templates/
│   ├── index.html
│   ├── add_transaction.html
│   ├── transactions.html
│   └── summary.html
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-link>
cd finance-system
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Run Application

```
python app.py
```

---

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔗 API Endpoints

| Method | Endpoint               | Description          |
| ------ | ---------------------- | -------------------- |
| POST   | /api/transactions      | Create transaction   |
| GET    | /api/transactions      | Get all transactions |
| PUT    | /api/transactions/<id> | Update transaction   |
| DELETE | /api/transactions/<id> | Delete transaction   |
| GET    | /api/summary           | Get summary          |

---

## 📊 Example Output

```
Total Income: 1000
Total Expense: 500
Balance: 500
```

---

## 🧠 Design Approach

* Modular structure using Blueprints
* Separation of concerns (routes, services, utils)
* Validation handled in a dedicated module
* Database abstraction using SQLAlchemy
* Hybrid system (API + frontend templates)

---

## ⚠️ Assumptions

* Transaction amount must always be positive
* Transaction type defines income or expense
* Basic implementation without authentication (can be extended)

---

## 🌟 Future Enhancements

* User authentication (JWT / session-based)
* Role-based access (Admin, Analyst, Viewer)
* Filtering and search functionality
* Pagination for large datasets
* Data export (CSV/JSON)
* Dashboard with charts

---

## 👨‍💻 Author

**Prafulla Bhusal**

---

## 📌 Conclusion

This project demonstrates strong backend development skills using Flask, including API design, database handling, validation, and integration with frontend templates. It provides a clean and maintainable solution for financial record management.
