# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM tiangolo/uvicorn-gunicorn:python3.8-slim

RUN apt update -y
RUN apt install gcc -y

RUN adduser --disabled-password --gecos '' api
USER api

COPY --chown=api:api requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir --user

ENV PATH="/home/api/.local/bin:${PATH}"

COPY --chown=api:api src/ /app

WORKDIR /app

EXPOSE 8080

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8080", "--log-level", "warning", "--root-path", "/fast-api-template/v1"]
