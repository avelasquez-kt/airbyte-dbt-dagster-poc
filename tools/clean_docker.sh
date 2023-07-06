#!/bin/bash

# Stop all containers
docker stop $(docker ps -a -q)

# Remove all containers
docker rm $(docker ps -a -q)

# Remove all iimages
docker rmi $(docker images -a -q)

# Remove all volumes
docker volume prune -a

# System cleanup
docker system prune -a