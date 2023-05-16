pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'shivyanshgarg05'
        DOCKER_PASSWORD = 'SPE@123456'
        registryCredential = 'dockerhub'
        registry_backend = 'shivyanshgarg05/backend'
        registry_frontend = 'shivyanshgarg05/frontend'
    }

    stages {
        stage('Github Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/shivgarg05/spemajor'
            }
        }

        
        stage('Build Images') {
            steps {
              
                sh 'docker build -t shivyanshgarg05/backend ./backend'
                sh 'docker build -t shivyanshgarg05/frontend ./frontend'

             
            }
        }
        
        stage('Push Images to DockerHub') {
            steps {
                sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                sh 'docker push shivyanshgarg05/backend'
                sh 'docker push shivyanshgarg05/frontend'
            }
        }

       
        
        stage('Kubernetes') {
            steps {
                sh "kubectl apply -f backend/k8s/secretkeys.yaml --kubeconfig=${env.KUBECONFIG_PATH}"
                sh "kubectl apply -f backend/k8s/config.yaml --kubeconfig=${env.KUBECONFIG_PATH}"
                sh "kubectl apply -f backend/k8s/mysql-db.yaml --kubeconfig=${env.KUBECONFIG_PATH}"
                sh "kubectl apply -f backend/k8s/myblog-job.yaml --kubeconfig=${env.KUBECONFIG_PATH}"
                sh "kubectl apply -f backend/k8s/backend.yaml --kubeconfig=${env.KUBECONFIG_PATH}"
                sh "kubectl apply -f backend/k8s/frontend.yaml --kubeconfig=${env.KUBECONFIG_PATH}"
                sh "kubectl apply -f backend/k8s/ingress.yaml --kubeconfig=${env.KUBECONFIG_PATH}"
            }
        }
        
    }
}
