pipeline {
    agent any

    environment {
        IMAGE_NAME = 'web'
        PORT = '5002'
        HOST_PORT = '5002'
        SCORES_FILE = 'Scores.txt'
    }

    stages {
        stage('Environment') {
            steps {
                sh 'echo $PATH'
                sh 'which git'
            }
        }
        stage('Checkout') {
            steps {
                git 'https://github.com/adirahamim/WorldOfGames.git'
            }
        }
        // Other stages...
    }
}
