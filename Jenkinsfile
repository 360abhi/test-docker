pipeline {
  agent any

  stages {
    stage('Sanity Check') {
      steps {
        echo '✅ Jenkinsfile is working!'
        sh 'echo "Current Directory: $(pwd)"'
        sh 'ls -la'
      }
    }

    stage('Simulate Test') {
      steps {
        echo '🔍 Running dummy test...'
        sh 'echo "Pretend this is a test..."'
      }
    }
  }

  post {
    always {
      echo '🎯 Pipeline finished running.'
    }
  }
}
