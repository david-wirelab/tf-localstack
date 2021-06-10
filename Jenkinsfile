def withDockerNetwork(Closure inner) {
  try {
    networkId = UUID.randomUUID().toString()
    sh "docker network create ${networkId}"
    inner.call(networkId)
  } finally {
    sh "docker network rm ${networkId}"
  }
}

pipeline {
  agent any

  stages {
    stage("Run Terraform tests") {
      steps {
        script {
            sh '''
            docker network create boo
            docker run -d --network boo --name localstack -p 4566:4566 -p 4571:4571 localstack/localstack
            docker run -d --network boo wirelab/terraform-testrunner:9 sh -c "python -m unittest tests/*_test.py"
            '''
        }
      }
    }
  }
  post {
      always {
          cleanWs()
      }
  }
}
