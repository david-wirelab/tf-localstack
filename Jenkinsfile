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
  agent none

  // stages {
  //   stage("checkout scm") {
  //     agent any
  //     steps{
  //       checkout scm
  //     }
  //   }
    stage("test") {
      agent any
      steps {
        script {
          def tf_code = docker.image('wirelab/terraform-testrunner:9')
          def localstack = docker.image('localstack/localstack')

          withDockerNetwork{ n ->
            localstack.withRun("--network ${n} --name localstack -v /var/run/docker.sock:/var/run/docker.sock -p 4566:4566 -p 4571:4571") { c ->
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
