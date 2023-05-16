pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'shivyanshgarg05'
        DOCKER_PASSWORD = 'CHALSi@1234'
        registryCredential = 'dockerhub'
        registry_backend = 'pratikahirrao/backend'
        registry_frontend = 'pratikahirrao/frontend'
    }

    stages {
        stage('Github Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Pratik-ahirrao/spe_major_project/'
            }
        }

        
        stage('Build Images') {
            steps {
              
                bat 'docker build -t pratikahirrao/backend ./backend'
                bat 'docker build -t pratikahirrao/frontend ./frontend'

             
            }
        }
        
        stage('Push Images to DockerHub') {
            steps {
                // withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                // bat 'echo %DOCKER_USERNAME%'
                // bat 'echo %DOCKER_PASSWORD%'
                bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                bat 'docker push  pratikahirrao/backend'
                bat 'docker push pratikahirrao/frontend'
              
            }
        }

       
        
        stage ('Apply Kubernetes manifests') {
            steps {
                bat 'kubectl apply -f backend/k8s/secretkeys.yaml --kubeconfig=C:/Users/Dell/.kube/config'
                bat 'kubectl apply -f backend/k8s/config.yaml --kubeconfig=C:/Users/Dell/.kube/config'
                bat 'kubectl apply -f backend/k8s/mysql-db.yaml --kubeconfig=C:/Users/Dell/.kube/config'
                bat 'kubectl apply -f backend/k8s/myblog-job.yaml --kubeconfig=C:/Users/Dell/.kube/config' 
                bat 'kubectl apply -f backend/k8s/backend.yaml --kubeconfig=C:/Users/Dell/.kube/config'
                bat 'kubectl apply -f backend/k8s/frontend.yaml --kubeconfig=C:/Users/Dell/.kube/config'
                bat 'kubectl apply -f backend/k8s/ingress.yaml --kubeconfig=C:/Users/Dell/.kube/config'
            }
        }
        
    }
}
