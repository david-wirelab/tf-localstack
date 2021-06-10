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
            docker network create local
            docker run -d --network local --name localstack -p 4566:4566 -p 4571:4571 localstack/localstack
            docker run -d --network local wirelab/terraform-testrunner:9 sh -c "python -m unittest tests/*_test.py"
            docker network rm local
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
