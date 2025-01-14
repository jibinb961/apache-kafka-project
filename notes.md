## Random User Project

- First we install apache airflow python packge with the virtual env
- Next we, create a new folder called DAG, and dag stands for Directed Acyclic Graph which defines the workflow of a process that includes tasks and dependecies. 
- I have added a new pytyhon file in that called, kafka_streaming.py , which will handle the DAG operations through Airflow. 


## Setting up the Docker
- First we create the docker-compose yaml that contains the information about what all containers we need to spin up 
    - Zookeeper
    - Broker
    - Control center
    - Schema registry   --- Need to understand more on that. 

- Then we execute the command `docker compose up -d` and this will download (if not already) and spin up all the containers in the yaml in detached mode (-d) which allows us to continue execution without waiting for the command to complete. 

- Now we need to publish the data that we get from the API, to KAFKA.


