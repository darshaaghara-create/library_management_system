### 📚 Simple Library Management System

An interactive, command-line based Library Management System built entirely in Python. It allows administrators to manage a book catalog, while users can register, search, issue, and return books seamlessly.

---

### 📖 Table of Contents

- Features

- Built With

- How to Run

- Project Structure

- How It Works

- Important Note

- Future Improvements

- Author

---

### ✨ Features

| Feature | Description |
| :--- | :--- |
| 🔐 **Role-Based Access** | Completely separate menus and permissions for Admins and Users. |
| 🛠️ **Admin Controls** | Easily add, update, or delete books from the library's catalog. |
| 🔍 **Smart Search** | Utilizes a recursive algorithm to quickly find books by title or author. |
| 📤 **Book Issuance** | Users can issue books, with built-in checks to prevent issuing the same book twice. |
| 📜 **Transaction History** | Automatically tracks every book issued and returned by a specific user. |
| 👤 **User Authentication** | New users are automatically registered; returning users must enter their password. |
| 📊 **Book Counter** | Users can instantly see how many books they currently have checked out. |

### 🛠️ Built With

| Technology / Concept | Purpose |
| :--- | :--- |
| 🐍 **Python 3** | Core Logic and application execution. |
| 🗂️ **Data Structures** | - Dictionaries<br>- Sets<br>- Tuples<br>- Lists<br>*(Used for efficient in-memory data management)* |
| 🔄 **Recursion** | Implemented specifically for the book search functionality. |

---

### 🚀 How to Run

1. Follow these steps to get the application running on your local machine:

2. Check Prerequisites: Ensure you have Python 3 installed on your system.

3. Get the Code: Clone this repository or simply download the Python file.

4. Open Terminal: Open your terminal, command prompt, or Anaconda prompt.

5. Navigate: Move to the folder where the file is saved (cd path/to/folder).

6. Execute: Run the following command:
  - bash
    - python library_management_system.py

### 💡 Note: No external libraries are required. You do not need to run any pip install commands. The project uses only native Python features.

---

### 📂 Project Structure
Since this is a single-file application, the structure is straightforward:

text
LibrarySystem/
│
├── library_management_system.py   # The main Python script containing all logic
└── README.md                      # Project documentation

---

### ⚙️ How It Works

### 🔑 Admin Access

- Select 1 from the main menu.

- Log in using the default credentials:

  - Username: admin

  - Password: admin123

- From the Admin Menu, you can view, add, modify, or delete books.

### 🧑‍🎓 User Access

- Select 2 from the main menu.

- Enter your name and password. (If you are a new user, the system will automatically register you).

- Once logged in, you can:

  - Search the catalog

  - Issue books

  - Return books

  - View your personal transaction history

---

### ⚠️ Important Note

This is a front-end, console-based academic project. All data (books, members, issued logs) is currently stored in memory. When you close the program, the data will reset to the default state. There is no backend database connected at this time.

---

### 🔮 Future Improvements

□ Database Integration: Connect to SQLite or MySQL to save data permanently between sessions.
□ GUI: Build a visual interface using Tkinter or PyQt.
□ Web Application: Convert the logic to a web app using Flask or Django.
□ Date Tracking: Add due dates for issued books and calculate late fees.
□ Security: Implement secure password hashing instead of storing plain text.

---

### 👨‍💻 Author

- Darsha Aghar

---

### 📄 License

This project is for educational purposes only.
