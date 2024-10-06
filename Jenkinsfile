pipeline {
    agent any
    environment {
        COMPOSE_FILE = 'docker-compose.yml' // Nombre de tu archivo Docker Compose
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build' // Construye las imágenes de los servicios
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d' // Ejecuta el backend y Redis en segundo plano
            }
        }
    }
}
