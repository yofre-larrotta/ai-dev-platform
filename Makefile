.PHONY: up down logs restart ps build clean help

# Default target
.DEFAULT_GOAL := help

# Start all services
up:
	@echo "Starting all services..."
	docker-compose up -d
	@echo "Services started. Frontend: http://localhost:8080, Backend: http://localhost:5000"

# Stop all services
down:
	@echo "Stopping all services..."
	docker-compose down
	@echo "Services stopped."

# View logs
logs:
	@echo "Showing logs (Ctrl+C to exit)..."
	docker-compose logs -f

# Restart all services
restart:
	@echo "Restarting all services..."
	docker-compose restart
	@echo "Services restarted."

# Show service status
ps:
	@echo "Service status:"
	docker-compose ps

# Build or rebuild services
build:
	@echo "Building services..."
	docker-compose build
	@echo "Build complete."

# Clean up containers, networks, and volumes
clean:
	@echo "Cleaning up..."
	docker-compose down -v
	@echo "Cleanup complete."

# Show help
help:
	@echo "AI Development Platform - Docker Compose Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  up        Start all services in detached mode"
	@echo "  down      Stop all services"
	@echo "  logs      View logs from all services"
	@echo "  restart   Restart all services"
	@echo "  ps        Show service status"
	@echo "  build     Build or rebuild services"
	@echo "  clean     Stop services and remove containers, networks, and volumes"
	@echo "  help      Show this help message"
