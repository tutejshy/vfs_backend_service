## VFS service

### Roadmap
- Docker
  - docker-complose
- Python >= 3.8
- fastapi
  - starlett
  - pydantic
- python-dotenv
- uvicorn

### Dependencies
```console  
- fastapi         - web framework for building APIs
- pydantic        - data validation and settings management
- python-dotenv   - reads key-value pairs from a .env file 
- uvicorn         - lightning-fast ASGI server
```

### Installation
All variables must be registered in the .env file
```console
# PROJECT
PROJECT_NAME=<App name>
PROJECT_VERSION=<App version>     

# CORS - https://fastapi.tiangolo.com/tutorial/cors/
BACKEND_CORS_ORIGINS=["*"]
```
###Manual start
1 Create a virtual environment
```console
$python -m venv venv
```
2 Activate the virtual environment (use PyCharm and your can skip this step)
```console
$source venv/bin/activate
```
3 Install dependencies
```console
(venv)$pip install -r requirements.txt
```
4 Run a project
```console
(venv)$uvicorn app.main:app --reload --host 0.0.0.0 --port 4848
```
### Run it
```console
$docker-compose up --build -d  # build, d - optional params
```
All documentation on the methods is available at: http://localhost:4848/docs

### Run tests
```console
(venv)$pytest
```
### Skeleton
```console  
app
    ├── api                   - web related stuff
    │   ├── deps              - depends for api interface
    │   └── v1                - api interface
    │       └── routes        - web routes
    ├── core                  - application configuration
    └── main.py               - FastAPI application creation and configuration
```
### References
* [docker](https://www.docker.com/)
* [python](https://www.python.org/)
* [fastapi](https://fastapi.tiangolo.com/)
* [pydantic](https://pydantic-docs.helpmanual.io/)
* [uvicorn](https://www.uvicorn.org/)
