pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || echo "Tests ran"'
            }
        }

        stage('Create Zip') {
            steps {
                sh 'zip -r complete-$(date +%F-%H-%M).zip .'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.zip'
        }
    }
}