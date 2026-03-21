# 🏋️ ACEest Fitness & Gym Management System

## 📌 Project Overview

ACEest Fitness & Gym Management System is a Flask-based web application designed to manage gym clients, track fitness programs, and monitor user progress.

This project demonstrates modern **DevOps practices** including CI/CD pipelines, containerization, automated testing, and structured Git workflows.

---

## 🚀 Features

* Add and manage client details
* View client summary
* Select fitness programs:

  * Fat Loss
  * Muscle Gain
  * Beginner
* Responsive and clean UI using CSS
* Simple and user-friendly web interface

---

## 🎨 UI Enhancement

* Custom CSS styling added for better user experience
* Centered layout with card design
* Styled buttons and form inputs
* Improved readability and visual appearance

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
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
├── static/
│   └── style.css
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

* Automatically runs on push and pull requests
* Installs dependencies
* Executes Pytest

### 🔹 Jenkins

* Pulls code from GitHub repository
* Installs dependencies
* Runs tests using Pytest
* Configured with Poll SCM for automatic builds

---

## 🔀 Git Workflow

* Followed **feature branch strategy**:

  * feature/tests
  * feature/docker
  * feature/githubworkflow
  * feature/styles
  * feature/readme
* Each feature was developed independently and merged into `main`

---

## 📸 Screenshots *(Add before submission)*

* Flask UI (Styled)
* Docker running app
* GitHub Actions success
* Jenkins build success

---

## 🧠 DevOps Concepts Demonstrated

* Continuous Integration (CI)
* Automated Testing
* Containerization using Docker
* CI/CD pipelines using GitHub Actions and Jenkins
* Git branching and pull request workflow

---

## 👩‍💻 Author

**Mahalakshmi**

---

## ✅ Conclusion

This project successfully demonstrates how DevOps tools and practices can be integrated into application development, ensuring automation, consistency, and scalability.
