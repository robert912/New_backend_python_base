pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'echo Building...'
                bat '"C:\\Python39\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'echo Testing...'
                bat 'venv\\Scripts\\activate.bat && python -m pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying...'
                // Aquí iría su lógica de despliegue
            }
        }
    }
}