# Uup - You up?

A FastAPI-based service that checks HTTP and HTTPS status for given domains. This service helps you verify the availability and status of websites over both HTTP and HTTPS protocols.

## Features

- Check HTTP and HTTPS status for any domain
- Configurable timeout for requests
- Input validation for domain names
- Docker support for easy deployment
- Automated testing and CI/CD pipeline

## Installation

### Local Development

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Deployment

### Automated Deployment (CI/CD)

The project uses GitHub Actions for automated deployment with two workflows:

1. **Docker Image Build and Push**
   - Triggered on push to main branch
   - Builds Docker image
   - Pushes to DockerHub

2. **Server Deployment**
   - Triggered after successful Docker image build
   - Deploys the container to the target server
   - Uses SSH for secure deployment
   - Automatically updates the running container

Required GitHub Secrets:
- `DOCKERHUB_USERNAME`: Your DockerHub username
- `DOCKERHUB_TOKEN`: Your DockerHub access token
- `SERVER_HOST`: Target server hostname/IP
- `SERVER_USER`: SSH username
- `SERVER_SSH_KEY`: SSH private key
- `SERVER_SSH_PORT`: SSH port (default: 22)
- `CONTAINER_NAME`: Name for the Docker container
- `HOST_PORT`: Port to expose on the host
- `CONTAINER_PORT`: Port exposed by the container (default: 8000)

### Manual Deployment

1. Build the Docker image:
```bash
docker build -t uup .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 uup
```

## Usage

### Running the Application

Start the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Check Domain Status
```
GET /check?target=<domain>&timeout=<seconds>
```

Parameters:
- `target` (required): Domain to check (e.g., example.com)
- `timeout` (optional): Request timeout in seconds (default: 5)

Example request:
```bash
curl "http://localhost:8000/check?target=example.com&timeout=5"
```

Example response:
```json
{
    "target": "example.com",
    "http_status": 301,
    "https_status": 200
}
```

### API Documentation

- Swagger UI: `http://localhost:8000/docs`



