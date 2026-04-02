pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
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

        stage('Run Newman Tests') {
            steps {
                sh '''
                export PATH=/Users/lawadeolokun/.nvm/versions/node/v22.13.1/bin:$PATH
                npx newman run tests/postman/collection.json
                '''
            }
        }

        stage('Stop Container') {
            steps {
                sh 'docker stop $(docker ps -q --filter ancestor=inventory-api)'
            }
        }

        stage('Generate README') {
            steps {
                sh 'python3 generate_readme.py'
            }
        }

        stage('Create ZIP Archive') {
            steps {
                sh '''
                DATE=$(date +%Y-%m-%d-%H-%M)
                zip -r complete-$DATE.zip app Dockerfile Jenkinsfile requirements.txt
                '''
    }
}
    }
}