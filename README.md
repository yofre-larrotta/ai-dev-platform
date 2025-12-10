# AI Development Platform

Plataforma de desarrollo con inteligencia artificial que integra Ollama, Flask backend y React frontend.

## 📋 Requisitos Previos

- Docker
- Docker Compose
- Make (opcional, pero recomendado)

## 🚀 Inicio Rápido

### Usando Make (Recomendado)

```bash
# Iniciar todos los servicios
make up

# Ver logs de los servicios
make logs

# Detener todos los servicios
make down
```

### Usando Docker Compose Directamente

```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down
```

## 🏗️ Arquitectura

El proyecto consta de tres servicios principales:

1. **Ollama** (Puerto 11434): Servidor de modelos de IA
2. **Backend** (Puerto 5000): API Flask que interactúa con Ollama
3. **Frontend** (Puerto 8080): Aplicación React

## 📦 Servicios

### Frontend (React)
- **Puerto**: 8080
- **Tecnología**: React 18
- **Variables de entorno**:
  - `REACT_APP_API_URL`: URL del backend (default: http://backend:5000)
  - `NODE_ENV`: Entorno de ejecución

### Backend (Flask)
- **Puerto**: 5000
- **Tecnología**: Python 3.11 + Flask
- **Variables de entorno**:
  - `FLASK_APP`: app.py
  - `FLASK_ENV`: development
  - `OLLAMA_HOST`: http://ollama:11434
  - `LOG_LEVEL`: INFO

### Ollama
- **Puerto**: 11434
- **Tecnología**: Ollama (modelos de IA)

## 🔧 Desarrollo

### Desarrollar en el Frontend

```bash
cd frontend
npm install
npm start
```

La aplicación estará disponible en http://localhost:3000 (modo desarrollo local).

### Desarrollar en el Backend

```bash
cd backend
pip install -r requirements.txt
flask run
```

El backend estará disponible en http://localhost:5000.

## 📝 Comandos Útiles

```bash
# Ver estado de los contenedores
docker-compose ps

# Ver logs de un servicio específico
docker-compose logs -f frontend
docker-compose logs -f backend
docker-compose logs -f ollama

# Reconstruir un servicio específico
docker-compose up -d --build frontend

# Detener y eliminar volúmenes
docker-compose down -v

# Reiniciar un servicio
docker-compose restart frontend
```

## 🌐 Acceso a los Servicios

Una vez que todos los servicios estén ejecutándose:

- **Frontend**: http://localhost:8080
- **Backend API**: http://localhost:5000
- **Ollama API**: http://localhost:11434

## 🐛 Solución de Problemas

### El frontend no se conecta al backend

Verifica que el backend esté ejecutándose:
```bash
docker-compose ps
docker-compose logs backend
```

### Errores al construir el frontend

Limpia y reconstruye:
```bash
docker-compose down
docker-compose up -d --build frontend
```

### Problemas con Ollama

Espera a que Ollama termine de iniciar (puede tardar unos minutos):
```bash
docker-compose logs -f ollama
```

## 📄 Estructura del Proyecto

```
.
├── backend/              # Código del backend Flask
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/             # Código del frontend React
│   ├── public/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml    # Configuración de servicios
├── Makefile             # Comandos útiles
└── README.md            # Este archivo
```

## 📜 Licencia

Este proyecto está bajo licencia MIT.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
