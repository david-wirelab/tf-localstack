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
    stage("checkout scm") {
      steps{
        checkout scm
      }
    }
    stage("test") {
      steps {
        script {
          def tf_code = docker.image('wirelab/terraform-testrunner:9')
          def localstack = docker.image('localstack/localstack')

          withDockerNetwork{ n ->
            localstack.withRun("--network ${n} -v /var/run/docker.sock:/var/run/docker.sock --name localstack -p 4566:4566 -p 4571:4571") { c ->
              tf_code.inside("--network ${n} -v /var/run/docker.sock:/var/run/docker.sock") {
                sh "python -m unittest tests/*_test.py'"
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