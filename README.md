# AI Dev Platform

Una plataforma de desarrollo con integración de IA para asistencia en el desarrollo de software.

## Requisitos Previos

- [Docker](https://docs.docker.com/get-docker/) (versión 24.0 o superior recomendado)
- [Docker Compose](https://docs.docker.com/compose/install/) (incluido con Docker Desktop, o versión standalone v2)
- Python 3.11+ (para desarrollo local sin Docker)

> **Nota:** Los comandos en esta documentación usan la sintaxis `docker-compose`. Si usas Docker Compose v2 integrado, puedes usar `docker compose` (sin guión) como alternativa.

## Cómo Lanzar la Plataforma

### Usando Docker Compose (Recomendado)

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/yofre-larrotta/ai-dev-platform.git
   cd ai-dev-platform
   ```

2. **Iniciar todos los servicios:**
   ```bash
   docker-compose up -d
   ```

3. **Verificar que los servicios están corriendo:**
   ```bash
   docker-compose ps
   ```

4. **Acceder a la plataforma:**
   - Backend API: http://localhost:5000
   - Ollama API: http://localhost:11434

> **Nota:** El frontend está definido en `docker-compose.yml` pero requiere que se cree el directorio `frontend/` con su Dockerfile antes de usar todos los servicios. Para iniciar solo backend y Ollama:
> ```bash
> docker-compose up -d ollama backend
> ```

### Detener la Plataforma

```bash
docker-compose down
```

Para eliminar también los volúmenes de datos:
```bash
docker-compose down -v
```

## Cómo Ejecutar Pruebas

### Ejecutar Pruebas con Docker

```bash
docker-compose exec backend pytest
```

### Ejecutar Pruebas Localmente

1. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Ejecutar las pruebas:**
   ```bash
   pytest
   ```

4. **Ejecutar pruebas con cobertura:**
   ```bash
   pytest --cov=backend --cov-report=html
   ```

5. **Ejecutar solo pruebas unitarias:**
   ```bash
   pytest -m unit
   ```

6. **Ejecutar solo pruebas de integración:**
   ```bash
   pytest -m integration
   ```

## Desarrollo Local

### Configurar el Backend

1. **Navegar al directorio del backend:**
   ```bash
   cd backend
   ```

2. **Crear entorno virtual e instalar dependencias:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Iniciar el servidor de desarrollo:**
   ```bash
   flask run --host=0.0.0.0
   ```

### Variables de Entorno

Puedes configurar las siguientes variables de entorno:

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `FLASK_APP` | Archivo principal de Flask | `app.py` |
| `FLASK_ENV` | Entorno de ejecución | `development` |
| `OLLAMA_HOST` | URL del servicio Ollama | `http://ollama:11434` |
| `LOG_LEVEL` | Nivel de logging | `INFO` |

## Estructura del Proyecto

```
ai-dev-platform/
├── backend/                    # Servicio backend Flask
│   ├── Dockerfile              # Configuración Docker del backend
│   ├── requirements.txt        # Dependencias Python
│   └── integrations/           # Módulos de integración
│       └── git_integration.py  # Integración con Git
├── frontend/                   # Directorio frontend (por implementar)
├── docker-compose.yml          # Orquestación de servicios Docker
├── pytest.ini                  # Configuración de pytest
├── .gitignore                  # Archivos ignorados por Git
└── README.md                   # Esta documentación
```

> **Nota:** El directorio `frontend/` está referenciado en `docker-compose.yml` pero aún no ha sido implementado.

## Servicios

| Servicio | Puerto | Descripción | Estado |
|----------|--------|-------------|--------|
| Backend | 5000 | API Flask para lógica de negocio | ✅ Disponible |
| Frontend | 8080 | Interfaz de usuario | ⚠️ Por implementar |
| Ollama | 11434 | Servicio de IA local | ✅ Disponible |

## Solución de Problemas

### El servicio Ollama no inicia

Verifica que Docker tenga suficiente memoria asignada (mínimo 4GB recomendado).

```bash
docker-compose logs ollama
```

### Error de conexión entre servicios

Asegúrate de que todos los servicios estén en la misma red:

```bash
docker network ls
docker-compose ps
```

### Limpiar y reiniciar

Si encuentras problemas, puedes limpiar todo y comenzar de nuevo:

```bash
docker-compose down -v
docker system prune -f
docker-compose up -d --build
```

## Licencia

Este proyecto está bajo la licencia MIT.
