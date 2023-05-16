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
                sh 'git checkout main -- config'
                sh 'chmod 600 config'
                
                script {
                    env.KUBECONFIG_PATH = "${env.WORKSPACE}/config"
                }
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
        stage('Grant Permissions') {
            steps {
                sh "chmod 600 ${env.KUBECONFIG_PATH}"
                sh 'chmod 600 /home/shivyansh/.minikube/profiles/minikube/client.crt'
                sh 'chmod 600 /home/shivyansh/.minikube/profiles/minikube/client.key'
                sh 'chmod 600 /home/shivyansh/.minikube/ca.crt'
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
