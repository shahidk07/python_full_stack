# User Management System

A full-stack web application I built to manage user information with a simple form interface and persistent database storage.

## 🛠️ Technologies Used

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Python 3 + Flask | Web server & request handling |
| **Frontend** | HTML5 + CSS3 | User interface & styling |
| **Database** | SQLite3 | Data persistence |
| **Templating** | Jinja2 | Dynamic HTML rendering |

## 🔄 Project Flow

### 1. User Interaction
```
User opens browser
    ↓
Navigates to http://localhost:5000
    ↓
Sees form + existing users table
```

### 2. Form Submission
```
User enters name & email
    ↓
Clicks Submit button
    ↓
Form sends POST request to Flask app
```

### 3. Data Processing
```
Flask receives POST request
    ↓
Extracts name & email from form data
    ↓
Executes parameterized SQL INSERT query
    ↓
Database stores new user record
    ↓
Commits transaction
```

### 4. Response & Display
```
Flask redirects back to home page
    ↓
Executes SELECT query to fetch all users
    ↓
Jinja2 renders HTML template with user data
    ↓
Browser displays updated table with new user
```

## 📁 Project Structure

```
python_full_stack/
├── task1/
│   ├── app.py              # Flask application & routes
│   ├── database.db         # SQLite database
│   ├── README.md           # Task documentation
│   ├── static/
│   │   └── style.css       # CSS styling
│   └── templates/
│       └── index.html      # HTML template
└── .venv/                  # Virtual environment
```

## 🚀 Quick Start

1. **Activate virtual environment**
   ```bash
   source .venv/bin/activate
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   cd task1
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

## 💡 Key Features

- **Add Users**: Submit name and email through HTML form
- **View Users**: Display all users in a formatted table
- **Data Persistence**: SQLite stores user data permanently
- **SQL Injection Prevention**: Uses parameterized queries for security
