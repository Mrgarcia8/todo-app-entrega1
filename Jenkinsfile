pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Obteniendo código del repositorio...'
                checkout scm
            }
        }

        stage('Instalar dependencias (modo usuario)') {
            steps {
                echo 'Instalando dependencias sin usar venv...'
                sh '''
                    pip3 install --user --break-system-packages -r web/requirements.txt
                '''
            }
        }

        stage('Prueba de ejecución') {
            steps {
                echo 'Ejecutando prueba de la aplicación Flask...'
                sh '''
                    python3 web/app.py &
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

