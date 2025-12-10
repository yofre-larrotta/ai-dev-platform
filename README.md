# AI Development Platform

A comprehensive AI development platform with a Flask backend and React frontend, orchestrated using Docker Compose.

## Architecture

This platform consists of three main services:

- **Ollama**: AI model service running on port 11434
- **Backend**: Flask API server running on port 5000
- **Frontend**: React application running on port 8080

## Prerequisites

- Docker (version 20.10 or higher)
- Docker Compose (version 2.0 or higher)
- Make (optional, for convenience commands)

## Quick Start

### Using Make (Recommended)

```bash
# Start all services
make up

# View logs
make logs

# Stop all services
make down
```

### Using Docker Compose Directly

```bash
# Start all services in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

## Services

### Frontend (React)

- **URL**: http://localhost:8080
- **Description**: React-based user interface
- **Environment Variables**:
  - `REACT_APP_API_URL`: Backend API URL (default in Docker: http://backend:5000, default locally: http://localhost:5000)
  - `NODE_ENV`: Node environment (development/production)

### Backend (Flask)

- **URL**: http://localhost:5000
- **Description**: Flask API server with AI integrations
- **Health Check**: http://localhost:5000/api/health
- **Environment Variables**:
  - `FLASK_APP`: Flask application entry point
  - `FLASK_ENV`: Flask environment
  - `OLLAMA_HOST`: Ollama service URL
  - `LOG_LEVEL`: Logging level (INFO, DEBUG, etc.)

### Ollama

- **URL**: http://localhost:11434
- **Description**: AI model service
- **Environment Variables**:
  - `OLLAMA_HOST`: Host and port configuration

## Development

### Frontend Development

```bash
cd frontend
npm install
npm start
```

The frontend will be available at http://localhost:3000 in development mode.

### Backend Development

```bash
cd backend
pip install -r requirements.txt
flask run
```

The backend will be available at http://localhost:5000.

## Deployment

### Production Deployment

1. Build and start all services:
   ```bash
   docker-compose up -d --build
   ```

2. Verify all services are running:
   ```bash
   docker-compose ps
   ```

3. Check logs for any issues:
   ```bash
   docker-compose logs -f
   ```

### Stopping Services

```bash
# Stop services but keep data
docker-compose stop

# Stop and remove containers
docker-compose down

# Stop and remove containers, networks, and volumes
docker-compose down -v
```

## Troubleshooting

### Service Won't Start

1. Check if ports are already in use:
   ```bash
   lsof -i :8080  # Frontend
   lsof -i :5000  # Backend
   lsof -i :11434 # Ollama
   ```

2. View service logs:
   ```bash
   docker-compose logs [service-name]
   ```

### Frontend Can't Connect to Backend

1. Verify backend is running:
   ```bash
   curl http://localhost:5000/api/health
   ```

2. Check network connectivity:
   ```bash
   docker-compose exec frontend ping backend
   ```

### Rebuilding Services

If you make changes to the code or Dockerfile:

```bash
docker-compose up -d --build [service-name]
```

## Environment Variables

Create a `.env` file in the root directory to customize environment variables:

```env
# Backend
FLASK_ENV=development
LOG_LEVEL=INFO
OLLAMA_HOST=http://ollama:11434

# Frontend
NODE_ENV=development
REACT_APP_API_URL=http://localhost:5000
```

## Data Persistence

The Ollama service uses a named volume (`ollama_data`) to persist AI models and data. This ensures that downloaded models are retained between container restarts.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
