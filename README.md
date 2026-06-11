# SB Intern Assessment POC

## Overview

SB Intern Assessment POC is a lightweight assessment platform built to demonstrate how compliance and assessment questionnaires can be administered, scored, and stored using a simple web application.

The application allows an assessor to:

- Select an assessment
- Answer compliance-related questions
- Automatically calculate a compliance score
- Record observations and remarks
- Store assessment results in PostgreSQL
- Update previously submitted assessments for the same user

This project was developed as a Proof of Concept (POC) inspired by assessment workflows commonly used within Sunbird-based ecosystems.

---

## Architecture

The solution consists of three main components:

### Frontend

- HTML
- JavaScript
- Dynamic quiz rendering
- Compliance score calculation

### Backend

- Flask REST API
- Handles assessment submission
- Persists results into PostgreSQL

### Database

- PostgreSQL
- Stores assessment responses
- Maintains user assessment history

### Supporting Services

- Redis (available for future caching/session requirements)
- Kong API Gateway configuration (placeholder)

---

## Project Structure

```text
project-root/
│
├── app.py
├── index.html
├── docker-compose.yml
├── kong.yml
├── requirements.txt
│
├── quizzes/
│   ├── it_policy.json
│   ├── cloud_ops.json
│   ├── linux_basics.json
│   └── ...
│
└── README.md
```

---

## File Descriptions

### app.py

Flask backend application.

**Responsibilities**

- Exposes assessment submission endpoint
- Accepts JSON payloads
- Inserts assessment data into PostgreSQL
- Updates existing records if a user submits again
- Returns success/failure responses

**Endpoint**

```http
POST /submit_assessment
```

### index.html

Frontend assessment application.

**Features**

- User ID capture
- Phone number capture
- Assessment selection
- Dynamic question rendering
- Compliance percentage calculation
- Remarks capture
- Submission to Flask API

### docker-compose.yml

Starts required infrastructure services.

#### PostgreSQL

- Container: `sb-quiz-db`
- Database: `intern_assessment`
- User: `quiz_admin`
- Port: `5432`

#### Redis

- Container: `sb-quiz-cache`
- Port: `6379`

Currently included for future extensibility.

### kong.yml

Placeholder Kong Gateway configuration.

Can later be extended for:

- Authentication
- Rate limiting
- API routing
- Monitoring
- Logging

### requirements.txt

Python dependencies:

```text
Flask
Flask-Cors
psycopg2-binary
```

---

## Prerequisites

### Python

Python 3.10+

```bash
python --version
```

### Docker

```bash
docker --version
```

### Docker Compose

```bash
docker compose version
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd sb-intern-assessment-poc
```

### 2. Create Virtual Environment

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Starting Infrastructure

Start PostgreSQL and Redis:

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

Expected:

```text
sb-quiz-db
sb-quiz-cache
```

---

## Database Setup

Connect to PostgreSQL:

```bash
docker exec -it sb-quiz-db psql -U quiz_admin -d intern_assessment
```

Create the assessment table:

```sql
CREATE TABLE assessment_results (
    id SERIAL PRIMARY KEY,

    phone_number VARCHAR(20),

    user_id VARCHAR(100) UNIQUE,

    q1 BOOLEAN,
    q2 BOOLEAN,
    q3 BOOLEAN,
    q4 BOOLEAN,
    q5 BOOLEAN,
    q6 BOOLEAN,
    q7 BOOLEAN,
    q8 BOOLEAN,
    q9 BOOLEAN,
    q10 BOOLEAN,

    compliance_percentage NUMERIC,

    remarks TEXT,

    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Running the Backend

```bash
python app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

---

## Running the Frontend

### Option 1: Open Directly

Open `index.html` in your browser.

### Option 2: Serve Locally

```bash
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

---

## Assessment Workflow

1. Enter Phone Number
2. Enter User ID
3. Select Assessment
4. Click **Start Quiz**
5. Answer all questions
6. Add remarks
7. Click **Submit Quiz**
8. Compliance score is calculated automatically
9. Results are stored in PostgreSQL

---

## Assessment Scoring Logic

Each answer is mapped to a compliance value:

```json
{
  "label": "Yes",
  "compliant": true
}
```

Formula:

```text
(Number of compliant answers / Total questions) × 100
```

Example:

```text
8 compliant answers out of 10
Compliance Score = 80%
```

---

## API Reference

### Submit Assessment

**Request**

```http
POST /submit_assessment
Content-Type: application/json
```

**Example Payload**

```json
{
  "phone_number": "9876543210",
  "user_id": "USER001",
  "q1": true,
  "q2": false,
  "q3": true,
  "q4": true,
  "q5": true,
  "q6": false,
  "q7": true,
  "q8": true,
  "q9": false,
  "q10": true,
  "compliance_percentage": 70,
  "remarks": "User requires additional training."
}
```

**Success Response**

```json
{
  "success": true,
  "message": "Assessment saved successfully"
}
```

---

## Adding New Assessments

Create a new JSON file inside:

```text
quizzes/
```

Example:

```text
quizzes/networking.json
```

Sample format:

```json
{
  "questions": [
    {
      "id": "q1",
      "body": "Is firewall configured?",
      "options": [
        {
          "label": "Yes",
          "compliant": true
        },
        {
          "label": "No",
          "compliant": false
        }
      ]
    }
  ]
}
```

Then add the assessment to the dropdown in `index.html`.

---

## Future Enhancements

- User authentication and authorization
- Assessment history dashboard
- CSV export functionality
- Sunbird integration
- Redis caching implementation
- Kong API Gateway integration
- Role-based access control
- Analytics and reporting dashboard
- Mobile-responsive UI
- Assessment templates and management

---

## Technology Stack

| Layer | Technology |
|---------|------------|
| Frontend | HTML, JavaScript |
| Backend | Flask |
| Database | PostgreSQL |
| Cache | Redis |
| Containerization | Docker |
| API Gateway | Kong |
| Assessment Framework | Sunbird-inspired QuML Structure |

---

## License

This project is intended for educational, learning, and proof-of-concept purposes. It may be modified and extended as required.
