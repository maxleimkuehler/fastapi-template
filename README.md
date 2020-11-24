# Fast API Template
## Development Setup

Set up a virtual environment and install requirements:

```bash
python3 -m venv env
source env/bin/activate
make init
```

## Api Documentation

Open http://localhost:8080/docs in your browser.

## Docker

Create a `.docker.env` file for the docker and insert necessary environment variables.
```bash
API_KEY=12345
```

```bash
# Make sure .docker.env is present
make build

# Run docker
make run

# Stop docker
make stop

# Romove Dokcer
make remove

# Run as deamon
make run.d
make logs
```
