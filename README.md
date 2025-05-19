#Uup - You up?

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

### Docker Deployment

Build and run using Docker:
```bash
docker build -t uup .
docker run -p 8000:8000 uup
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

## Development

### Running Tests

```bash
pytest test_main.py -v
```

### CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Runs tests on every push and pull request
2. Builds and pushes Docker images to DockerHub Registry on:
   - Push to main branch

