pipeline {
    agent any

    stages {

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
    }
}