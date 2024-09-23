pipeline {
    agent any

    environment {
        IMAGE_NAME = 'web'
        PORT = '8777'
        HOST_PORT = '8777'
        SCORES_FILE = 'Scores.txt'
    }

    stages {
        stage('Clone Repository') {
            steps {
<<<<<<< HEAD
                git branch: 'main', url: 'https://github.com/adirahamim/WorldOfGames.git'
=======
                echo 'Checking out code...'
                git 'https://github.com/adirahamim/WorldOfGames.git'
>>>>>>> 31123e54890432d0af9cebb3b8f1c00e535ed94a
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
