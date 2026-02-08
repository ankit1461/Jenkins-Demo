pipeline {
    agent {label 'agent'}

    stages {
        stage('Code Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/ankit1461/Jenkins-Demo.git'
            }
        }

        stage('Build Images'){
            steps {
                sh 'docker compose build'
            }
        }

        stage('Build Container'){
            steps {
                sh 'docker compose down || true && docker compose up -d'
            }
        }
    }
}