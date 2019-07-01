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

- Containers: web(scalable), visualizer and Redis Db 
- Used python framework
  1. redis-py
  2. Flask
  3. render_template
- Deploy cmd
  `docker stack deploy -c docker-compose.yml <name>`
- Functions
  1. add new task 
  2. delete all tasklist
  3. view all tasks in list


