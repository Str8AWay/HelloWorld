node('jenkins-ecs') {
    stage('Checkout') {
        checkout scm
    }

    stage('Compile') {
        sh 'javac *.java'
    }

    stage('Test') {
        sh 'python HelloWorldTest.py'
    }

    stage('Archive') {
        archiveArtifacts '*.class'
    }
}
