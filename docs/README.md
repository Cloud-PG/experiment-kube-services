# DOCS

## Docker 

- Follow the guide from [https://docs.docker.com/get-started/]
- Set up your Docker environment
- Build an image
- Run a container
  `docker stack deploy -c docker-compose.yml getstartedlab`
- Scale 1 container to 10 replicas
- Install 2 VMs (one is manager and another one is worker)
- Distribute the app across a cluster
- Stack services 
  1. add Redis Db
  2. add visualizer

## Create a simple task list web stack

- Containers:
  web(scalable), visualizer and Redis Db 
- Used python framework
  1. redis-py
  2. Flask
  3. render_template
- Steps:
  1. Download all files from "To do list"
  2. Create a volumn for database in vm  
    `docker-machine ssh <vm name> "mkdir ./data"`
  3. Make sure the file contains Dockerfile, app.py, requirements.txt and templates  
    Build image by  `docker build --tag=<image name> .`  
    The image name should be the same with service:web:image: in docker-compose.yml file
  4. Start running  
    `docker swarm init`  
    `docker stack deploy -c docker-compose.yml <stack name>`
- Functions
  1. add new task 
  2. delete all tasklist
  3. view all tasks in list

## Simple task list on Kubernetes 

- Install kubectl and minikube
- Reused the image before
- Steps
  1. Start minikube
  2. Set the environment variables  
    `eval $(minikube docker-env) `
  3. Create a deployment  
    `kubectl create -f deployment hello-application.yml`  
    The deployment:spec:template:spec:containers:image should be same as the built docker local image
  4. Create a service and thus expose the deployment  
    `kubectl expose deployment hello-world --type=NodePort --name=tasklist-service`
  5. View the pods  
    `kubectl get pods --selector="run=load-balancer-example" --output=wide`
  6. Get the node address by `kubectl cluster-info` and node port by `kubectl describe services tasklist-service`
- Kubernetes Deployment includes the function from pods and replicaSet. It can by updated by `edit` and `apply` and do not need to stop the service.


## Blue/Green Deployments with Kubernetes and Istio

- Reused the image before
- Folder: BlueGreen
- Steps:
  1. Start minikube
  2. Install Istio  
  `curl -L https://git.io/getLatestIstio | sh -`  
  spec:type -> NodePort
  3. Create 1 service, 2 deployments  
  `kubectl create -f myapp.yaml`  
  4. Create redis StatefulSet and its service (port 6379)  
  `kubectl create -f redis.yml`
  5. Configurate istio routing by  
  `kubectl port-forward deployment/<name of deployment> 8080:80`  
  The simple tasklist website is visted at localhost:8080
- To route the traffic base on weight  
  Step:  
  1. Create a gate way  
  `kubectl apply -f app-gateway.yaml `  
  Weight can be modified in this files
  2. Submit it to istio  
  `istioctl replace -f app-gateway.yaml`
  3. Run to access the Ingress Host (Minikube) and Ingress port.
  `export INGRESS_HOST=$(minikube ip)`  
  `export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')`
- Problems may exist:
  It run slower when it run longer time.
  Now the two images of v1 and v2 is the same.



