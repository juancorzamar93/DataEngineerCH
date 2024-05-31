# Variables
DOCKER_COMPOSE=docker-compose
COMPOSE_FILE=docker-compose.yml

# Objetivos
.PHONY: build up down logs

# Construir imágenes Docker
build:
    $(DOCKER_COMPOSE) -f $(COMPOSE_FILE) build

# Levantar servicios Docker Compose
up:
    $(DOCKER_COMPOSE) -f $(COMPOSE_FILE) up -d

# Detener servicios Docker Compose
down:
    $(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down

# Ver logs de los servicios
logs:
    $(DOCKER_COMPOSE) -f $(COMPOSE_FILE) logs -f
