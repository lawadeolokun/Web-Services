pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t inventory-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '/usr/local/bin/docker run -d -p 8000:8000 inventory-api'
            }
        }
    }
}