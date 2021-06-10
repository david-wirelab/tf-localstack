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
          withDockerNetwork{ n ->
            sh '''
            docker run -d \
            --network ${n} \
            --name localstack \
            -p 4566:4566 \
            -p 4571:4571 \
            localstack/localstack
            ''' { c ->
              sh '''
              docker run -d \
              --network ${n} \
              wirelab/terraform-testrunner:9
              ''' {
                sh "python -m unittest tests/*_test.py"
              }
            }
          }
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
