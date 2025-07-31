#!/bin/bash

# This script creates a development Docker container for api-home
# It mounts the local directory to allow for live code editing
# The service will automatically restart when files are modified (hot-reload)

# Stop and remove the existing container if it exists
docker stop karned-api-home || true
docker rm karned-api-home || true

# Run the container with local directory mounted
docker run -d \
  --name karned-api-home \
  --network karned-network \
  -p 9008:8000 \
  -v "$(pwd):/app" \
  -e KEYCLOAK_HOST=http://karned-keycloak:8080 \
  -e KEYCLOAK_REALM=karned \
  -e KEYCLOAK_CLIENT_ID=karned \
  -e KEYCLOAK_CLIENT_SECRET=secret \
  -e REDIS_HOST=karned-redis \
  -e REDIS_PORT=6379 \
  -e REDIS_DB=0 \
  -e REDIS_PASSWORD= \
  -e URL_API_GATEWAY=http://api-gateway-service \
  -e API_NAME=api-home \
  -e API_TAG_NAME=homes \
  killiankopp/api-home:1.0.0 \
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload

echo "Development container started. Your local code is mounted at /app in the container."
echo "Hot-reload is enabled - the service will automatically restart when files are modified."
echo "Access the API at http://localhost:9008"
echo "To view logs: docker logs karned-api-home"
echo "To stop: docker stop karned-api-home"
