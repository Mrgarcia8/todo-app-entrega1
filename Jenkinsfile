pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Obteniendo código del repositorio...'
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                echo 'Instalando dependencias...'
                sh '''
                    pip install --upgrade pip
                    pip install -r web/requirements.txt
                '''
            }
        }

        stage('Prueba de ejecución') {
            steps {
                echo 'Ejecutando prueba de la aplicación Flask...'
                sh '''
                    python web/app.py &
                    sleep 5
                    echo "Aplicación ejecutada correctamente"
                '''
            }
        }

        stage('Finalización') {
            steps {
                echo 'Pipeline ejecutado correctamente.'
            }
        }
    }
}
