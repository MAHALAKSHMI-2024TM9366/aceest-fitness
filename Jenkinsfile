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

        stage('SonarQube Analysis') {
    steps {
        sh '''
        docker run --rm \
        -e SONAR_HOST_URL="http://host.docker.internal:9000" \
        -e SONAR_TOKEN="squ_2dfb825d8c4f8af41d8aab5f7a27d22c9c78be57" \
        -v "$PWD:/usr/src" \
        sonarsource/sonar-scanner-cli \
        -Dsonar.projectKey=aceest-fitness \
        -Dsonar.sources=. \
        -Dsonar.python.coverage.reportPaths=coverage.xml
        '''
    }
}
    }
}