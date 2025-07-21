pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'    // Uses your Dockerfile
      dir '.'                  // Context directory (where Dockerfile is)
      additionalBuildArgs ''
    }
  }

  stages {
    stage('Run Playwright Tests') {
      steps {
        sh 'pytest Playwright/jobs/test_play.py --html=Playwright/jobs/report.html'
      }
    }

    stage('Archive Report') {
      steps {
        archiveArtifacts artifacts: 'Playwright/jobs/report.html', allowEmptyArchive: true
      }
    }
  }

//   post {
//     always {
//       emailext(
//         subject: "Playwright Test Report",
//         body: "Find the attached test report.",
//         to: "abhishekch360@gmail.com",
//         attachmentsPattern: 'Playwright/jobs/report.html'
//       )
//     }
//   }
}
