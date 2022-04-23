FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Fabio Almeida"

COPY ./web_app /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn","app:app", "--host", "0.0.0.0", "--port", "80"]
