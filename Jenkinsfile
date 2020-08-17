pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh './build/build.sh'
            }
        }
        stage('Test'){
            steps {
                sh 'pytest'
            }
        }
        stage('Approval') {
            steps {
                input "Shall the build be ${currentBuild.fullDisplayName} deployed to production?"
            }
        }
        stage('Production') {
            steps{
                echo 'Final step of the pipeline'
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
