FROM python:3.10.7-slim-buster

WORKDIR /app

COPY receiver.py receiver.py

RUN python -m pip install pika --upgrade

CMD python -u receiver.py