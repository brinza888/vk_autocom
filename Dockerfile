FROM python:3.10-alpine


COPY requirements.txt app/
RUN pip install -r app/requirements.txt

COPY main.py app/
COPY config.py app/

WORKDIR app

ENTRYPOINT ["python", "main.py"]
