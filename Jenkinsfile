pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-ecommerce-app"
        DOCKER_IMAGE = "shivavaddi/flask-ecommerce-app"
        CONTAINER_NAME = "flask-container"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/shiva-6300/End-to-End-CI-CD-Pipeline-for-Python-Application.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh 'docker tag $IMAGE_NAME:latest $DOCKER_IMAGE:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $DOCKER_IMAGE:latest'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $DOCKER_IMAGE:latest'
            }
        }

    }
}