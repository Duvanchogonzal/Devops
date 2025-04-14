pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Iniciando pipeline local con Docker Compose...'
            }
        }

        stage('Apagar contenedores previos') {
            steps {
                dir('/var/lib/jenkins/workspace/Proyecto_devops') {
                    sh 'docker-compose down || true'
                }
            }
        }

        stage('Construir contenedores') {
            steps {
                dir('/var/lib/jenkins/workspace/Proyecto_devops') {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Levantar aplicación') {
            steps {
                dir('/var/lib/jenkins/workspace/Proyecto_devops') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Verificar contenedores') {
            steps {
                sh 'docker ps -a'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
    }
}
 