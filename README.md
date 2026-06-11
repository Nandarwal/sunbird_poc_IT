# Sunbird Assessment POC

A simple assessment platform inspired by Sunbird architecture. Users enter their phone number, select a quiz, attempt the quiz, and their score is stored in PostgreSQL.

---

## Features

* Multiple quiz support
* Phone number based quiz attempts
* Dynamic quiz loading from JSON files
* Flask backend API
* PostgreSQL database storage
* Docker-based infrastructure
* Easily extensible architecture

---

## Project Structure

```text
sunbird-poc/
│
├── quizzes/
│   ├── cloud_ops.json
│   ├── linux_basics.json
│   ├── networking.json
│   ├── database_basics.json
│   └── sunbird_intro.json
│
├── app.py
├── index.html
├── docker-compose.yml
├── kong.yml
├── requirements.txt
└── README.md
```

---

## Prerequisites

Before running the project, ensure the following are installed:

### Python 3.10+

Verify installation:

```bash
python3 --version
```

### Docker Desktop

Install Docker Desktop and ensure it is running.

Verify installation:

```bash
docker --version
docker compose version
```

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/Nandarwal/sunbird_os_poc.git
```

Move into the project directory:

```bash
cd sunbird-poc
```

---

## Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate it:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Step 3: Install Python Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Step 4: Start PostgreSQL Using Docker

Start the database container:

```bash
docker compose up -d
```

Verify the container is running:

```bash
docker ps
```

You should see:

```text
sb-quiz-db
```

---

## Step 5: Create Database Table

Connect to PostgreSQL:

```bash
docker exec -it sb-quiz-db psql -U quiz_admin -d intern_assessment
```

Create the table:

```sql
CREATE TABLE IF NOT EXISTS quiz_results (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(20),
    quiz_id VARCHAR(100),
    quiz_name VARCHAR(200),
    score INTEGER,
    total_questions INTEGER,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Verify:

```sql
\dt
```

Exit PostgreSQL:

```sql
\q
```

---

## Step 6: Start the Flask Backend

Run:

```bash
python app.py
```

You should see:

```text
Running on http://127.0.0.1:5000
```

Keep this terminal open.

---

## Step 7: Start the Frontend

Open a second terminal window.

Navigate to the project folder:

```bash
cd sunbird-poc
```

Start a local web server:

```bash
python -m http.server 8000
```

---

## Step 8: Open the Application

Open your browser and visit:

```text
http://localhost:8000/index.html
```

---

## Step 9: Use the Application

1. Enter your phone number
2. Select a quiz
3. Click "Start Quiz"
4. Attempt the quiz
5. Click "Submit Quiz"
6. View your score

---

## Step 10: Verify Results in PostgreSQL

Open a new terminal:

```bash
docker exec -it sb-quiz-db psql -U quiz_admin -d intern_assessment
```

Run:

```sql
SELECT * FROM quiz_results;
```

You should see stored quiz attempts including:

* Phone Number
* Quiz Name
* Score
* Submission Timestamp

---

## Stopping the Application

Stop the database container:

```bash
docker compose down
```

Deactivate the Python virtual environment:

```bash
deactivate
```

---

## Tech Stack

* Frontend: HTML, JavaScript
* Backend: Flask
* Database: PostgreSQL
* Infrastructure: Docker
* Optional Components: Redis, Kong Gateway

---

## Future Enhancements

* Backend score calculation
* Leaderboard support
* User attempt history
* Quiz analytics dashboard
* Kong API Gateway integration
* Authentication and authorization