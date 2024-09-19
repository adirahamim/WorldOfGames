pipeline {
    agent any

    environment {
        IMAGE_NAME = 'worldofgames-web'
        PORT = '5002'
        HOST_PORT = '5002'
        SCORES_FILE = 'Scores.txt'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/adirahamim/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}").run("-p ${HOST_PORT}:${PORT} -v $PWD/${SCORES_FILE}:/Scores.txt")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('Tests failed')
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh "docker stop \$(docker ps -q --filter ancestor=${IMAGE_NAME})"
                    docker.image("${IMAGE_NAME}").push()
                }
            }
        }
    }
    post {
        always {
            script {
                def containers = sh(script: "docker ps -q --filter ancestor=${IMAGE_NAME}", returnStdout: true).trim()
                if (containers) {
                    sh "docker rm -f ${containers}"
                }
            }
        }
    }
}
