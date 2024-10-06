pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'echo Building...'
                bat 'python -m venv venv'
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
                // Por ejemplo:
                // bat 'docker build -t my-python-app .'
                // bat 'docker run -d -p 5000:5000 my-python-app'
            }
        }
    }
}
