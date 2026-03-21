# 🏋️ ACEest Fitness & Gym Management System

## 📌 Project Overview

ACEest Fitness & Gym Management System is a Flask-based web application designed to manage gym clients, track fitness programs, and monitor user progress.
This project demonstrates core **DevOps practices** such as CI/CD, containerization, and automated testing.

---

## 🚀 Features

* Add and manage client details
* View client summary
* Select fitness programs:

  * Fat Loss
  * Muscle Gain
  * Beginner
* Simple and user-friendly web interface

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML
* **Testing:** Pytest
* **Containerization:** Docker
* **CI/CD:** GitHub Actions, Jenkins
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
aceest-fitness/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── templates/
│   ├── index.html
│   ├── client.html
│   └── summary.html
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── main.yml
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/MAHALAKSHMI-2024TM9366/aceest-fitness.git
cd aceest-fitness
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the application

```
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🧪 Run Tests

```
python -m pytest
```

---

## 🐳 Docker Setup

### Build Docker Image

```
docker build -t aceest-fitness .
```

### Run Docker Container

```
docker run -p 5000:5000 aceest-fitness
```

### Access Application

```
http://localhost:5000
```

---

## 🔄 CI/CD Pipeline

### 🔹 GitHub Actions

* Automatically triggers on **push** and **pull requests**
* Installs dependencies
* Runs automated tests using Pytest

### 🔹 Jenkins

* Pulls code from GitHub repository
* Installs dependencies
* Runs test cases using Pytest
* Can be configured to trigger builds automatically (Poll SCM)

---

## 🔀 Git Workflow

* Used **feature branches** for each development step:

  * feature/step-1-flask
  * feature/step-2-tests
  * feature/step-3-docker
  * feature/step-4-github-actions
  * feature/step-5-jenkins
* Merged into `main` branch via commits / pull requests

---

## 📸 Screenshots

*(Add these before submission)*

* Flask application UI
* Docker running container
* GitHub Actions pipeline success
* Jenkins build success

---

## 🧠 DevOps Concepts Demonstrated

* Continuous Integration (CI)
* Automated Testing
* Containerization using Docker
* CI/CD pipelines using GitHub Actions and Jenkins
* Version control with Git

---

## 👩‍💻 Author

**Mahalakshmi**

---

## ✅ Conclusion

This project successfully demonstrates how modern DevOps tools and practices can be integrated into a web application development lifecycle, ensuring automation, reliability, and scalability.
