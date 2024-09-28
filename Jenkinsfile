pipeline {
    agent any

    environment {
        IMAGE_NAME = 'web'
        PORT = '8777'
        HOST_PORT = '8777'
        SCORES_FILE = 'Scores.txt'
    }

    stages {
        stage('Install pip') {
            steps {
                sh 'apt-get update && apt-get install -y python3-pip'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/adirahamim/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Building Docker image...'
                    docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    echo 'Running Docker container...'
                    docker.image("${IMAGE_NAME}").run("-p ${HOST_PORT}:${PORT} -v ${WORKSPACE}/${SCORES_FILE}:/Scores.txt")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        echo 'Test script failed with exit code: ' + result
                        error('Tests failed')
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    echo 'Finalizing...'
                    sh "docker stop \$(docker ps -q --filter ancestor=${IMAGE_NAME})"
                    docker.image("${IMAGE_NAME}").push()
                }
            }
        }
    }
    post {
        always {
            script {
                echo 'Cleaning up...'
                def containers = sh(script: "docker ps -q --filter ancestor=${IMAGE_NAME}", returnStdout: true).trim()
                if (containers) {
                    sh "docker rm -f ${containers}"
                }
            }
        }
    }
}
