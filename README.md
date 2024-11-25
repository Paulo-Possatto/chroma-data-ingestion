```
 ██████ ██   ██ ██████   ██████  ███    ███  █████  ███    ███  ██████  ███    ██ 
██      ██   ██ ██   ██ ██    ██ ████  ████ ██   ██ ████  ████ ██    ██ ████   ██ 
██      ███████ ██████  ██    ██ ██ ████ ██ ███████ ██ ████ ██ ██    ██ ██ ██  ██ 
██      ██   ██ ██   ██ ██    ██ ██  ██  ██ ██   ██ ██  ██  ██ ██    ██ ██  ██ ██ 
 ██████ ██   ██ ██   ██  ██████  ██      ██ ██   ██ ██      ██  ██████  ██   ████ 
```

# chroma-data-ingestion
This service is responsible for reading the data from the Excel file or the JSON object and persist the data.

## Initiate service:
The RabbitMQ and MongoDB will be initiated using [docker](https://www.docker.com/get-started/) with the following commands:

**RabbitMQ:**
``` bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```
The user and password will be both "guest", and you can check the queues and stream on your **localhost:15672**

---

**MongoDB:**
``` bash
docker run -d --name mongodb -p 27017:27017 mongo:latest
```
To verify the documents inserted on MongoDB, it's better to use [MongoDB Compass](https://www.mongodb.com/products/tools/compass), then you add the URI for the database connection: **localhost:27017**

---

When the MongoDB and RabbitMQ services are running, start the program with this command:
```bash
uvicorn main:app --reload
```