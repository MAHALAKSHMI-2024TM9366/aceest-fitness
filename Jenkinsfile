pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/MAHALAKSHMI-2024TM9366/aceest-fitness.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t aceest-fitness .
                '''
            }
        }
    }
}