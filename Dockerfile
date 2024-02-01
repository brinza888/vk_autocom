FROM python:3.10-alpine

COPY main.py app/
COPY config.py app/
COPY requirements.txt app/

WORKDIR app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
