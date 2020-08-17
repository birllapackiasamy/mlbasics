pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh './build/build.sh'
                sh 'pytest'
            }
        }
    }
    post{
        always{
            echo 'Pipeline processed'
        }
        success {
            echo 'Pipeline is successful'
        }
        failure {
            echo 'Pipeline got failed'
        }
    }
}
