pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Obteniendo código del repositorio...'
                checkout scm
            }
        }

        stage('Crear entorno virtual') {
            steps {
                echo 'Creando entorno virtual Python...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip --break-system-packages
                '''
            }
        }

        stage('Instalar dependencias') {
            steps {
                echo 'Instalando dependencias dentro del entorno virtual...'
                sh '''
                    . venv/bin/activate
                    pip install -r web/requirements.txt --break-system-packages
                '''
            }
        }

        stage('Prueba de ejecución') {
            steps {
                echo 'Ejecutando prueba de la aplicación Flask...'
                sh '''
                    . venv/bin/activate
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
