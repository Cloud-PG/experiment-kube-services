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


