pipeline {
  agent any

  environment {
    IMAGE = "tuusuario/todo-app"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python & Tests') {
      steps {
        sh 'python3 --version || true'
        sh '''
          python3 -m venv venv || true
          . venv/bin/activate
          python -m pip install --upgrade pip
          pip install -r web/requirements.txt
          pip install pytest coverage codecov
          coverage run -m pytest -q || true
          coverage xml -i || true
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          sh "docker build -f web/Dockerfile -t ${IMAGE}:latest ."
        }
      }
    }

    stage('Push Docker Image') {
      when {
        expression { return env.DOCKER_PUSH == 'true' }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
          sh "docker push ${IMAGE}:latest"
        }
      }
    }

    stage('Upload coverage to Codecov') {
      steps {
        withCredentials([string(credentialsId: 'codecov-token', variable: 'CODECOV_TOKEN')]) {
          sh '. venv/bin/activate || true; python -m pip install codecov || true; codecov -t $CODECOV_TOKEN || true'
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
    }
  }
}

