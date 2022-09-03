#!/bin/bash
JOIN_RABBIT1="rabbitmqctl stop_app; rabbitmqctl join_cluster rabbit@rabbitmq1; rabbitmqctl start_app"
 
 
echo -n "Starting container..."
docker-compose down
docker-compose up -d
sleep 15
docker exec -ti rabbitmq2 bash -c "$JOIN_RABBIT1"
docker exec -ti rabbitmq3 bash -c "$JOIN_RABBIT1"
docker exec -ti rabbitmq4 bash -c "$JOIN_RABBIT1"
docker exec -ti rabbitmq5 bash -c "$JOIN_RABBIT1"
