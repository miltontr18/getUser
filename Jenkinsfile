pipeline {
    environment {
        registry = "miltontr86/getuser_app"
        registryCredential = "dockerhub"
        dockerImage = ""
    }
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/miltontr18/getUser.git']])
                echo("Image successfully Checked out from GitHub.")
            }
        }
        stage('Build') {
            steps {
                script {
                    img = registry + ":$BUILD_NUMBER"
                    dockerImage = docker.build img
                    echo("Image ${img} successfully built")
                }
            }
        }
                stage('Test image') {
            steps {
                script {
                    container = "$JOB_NAME"+"-$BUILD_NUMBER"
                    bat "docker run --name ${container} -p 5000:5000 -d ${img}"
                    echo "${container} container successfully running !"
                }
            }
        }
        stage('Push to Dockerhub') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                        echo("Image ${img} successfully pushed to Dockerhub")
                    }
                }
            }
        }
    }
    post {
        always {
            bat "docker stop ${container}"
            echo "${container} container stopped successfully !"

            bat "docker rm ${container}"
            echo "${container} container successfully removed from Docker desktop"

            bat "docker rmi ${img}"
            echo("Image ${img} successfully deleted from docker desktop")
        }
    }
}