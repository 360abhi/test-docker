pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
      dir '.'
    }
  }

  stages {
    stage('Run Playwright Tests') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest Playwright/jobs/test_play.py --html=Playwright/jobs/report.html'
      }
    }

    stage('Archive Report') {
      steps {
        archiveArtifacts artifacts: 'Playwright/jobs/report.html', allowEmptyArchive: true
      }
    }
  }
}
