.PHONY: up down logs restart ps build clean help

# Colores para mensajes
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m # No Color

help: ## Muestra esta ayuda
	@echo "$(BLUE)AI Development Platform - Makefile Commands$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""

up: ## Inicia todos los servicios en segundo plano
	@echo "$(BLUE)Iniciando servicios...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✓ Servicios iniciados$(NC)"
	@echo "Frontend: http://localhost:8080"
	@echo "Backend: http://localhost:5000"
	@echo "Ollama: http://localhost:11434"

down: ## Detiene y elimina todos los contenedores
	@echo "$(BLUE)Deteniendo servicios...$(NC)"
	docker-compose down
	@echo "$(GREEN)✓ Servicios detenidos$(NC)"

logs: ## Muestra los logs de todos los servicios (Ctrl+C para salir)
	docker-compose logs -f

logs-frontend: ## Muestra los logs del frontend
	docker-compose logs -f frontend

logs-backend: ## Muestra los logs del backend
	docker-compose logs -f backend

logs-ollama: ## Muestra los logs de ollama
	docker-compose logs -f ollama

restart: ## Reinicia todos los servicios
	@echo "$(BLUE)Reiniciando servicios...$(NC)"
	docker-compose restart
	@echo "$(GREEN)✓ Servicios reiniciados$(NC)"

ps: ## Muestra el estado de los servicios
	docker-compose ps

build: ## Reconstruye todos los servicios
	@echo "$(BLUE)Reconstruyendo servicios...$(NC)"
	docker-compose build
	@echo "$(GREEN)✓ Servicios reconstruidos$(NC)"

build-frontend: ## Reconstruye solo el frontend
	@echo "$(BLUE)Reconstruyendo frontend...$(NC)"
	docker-compose build frontend
	@echo "$(GREEN)✓ Frontend reconstruido$(NC)"

build-backend: ## Reconstruye solo el backend
	@echo "$(BLUE)Reconstruyendo backend...$(NC)"
	docker-compose build backend
	@echo "$(GREEN)✓ Backend reconstruido$(NC)"

rebuild: down build up ## Reconstruye y reinicia todos los servicios

clean: ## Detiene servicios y elimina volúmenes
	@echo "$(YELLOW)⚠ Esto eliminará todos los volúmenes y datos$(NC)"
	@read -p "¿Estás seguro? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		docker-compose down -v; \
		echo "$(GREEN)✓ Servicios y volúmenes eliminados$(NC)"; \
	else \
		echo "Operación cancelada"; \
	fi

stop: ## Detiene los servicios sin eliminar contenedores
	@echo "$(BLUE)Deteniendo servicios...$(NC)"
	docker-compose stop
	@echo "$(GREEN)✓ Servicios detenidos$(NC)"

start: ## Inicia los servicios previamente detenidos
	@echo "$(BLUE)Iniciando servicios...$(NC)"
	docker-compose start
	@echo "$(GREEN)✓ Servicios iniciados$(NC)"

dev-frontend: ## Accede al shell del contenedor frontend
	docker-compose exec frontend sh

dev-backend: ## Accede al shell del contenedor backend
	docker-compose exec backend bash

status: ps ## Alias para ps

.DEFAULT_GOAL := help
