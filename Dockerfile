# syntax=docker/dockerfile:1
FROM python:3.10.8-bullseye
EXPOSE 8000

RUN apt install git
RUN apt-get update
RUN pip install --upgrade pip

ENV requirements=requirements.txt

COPY $requirements $requirements
COPY main.py main.py
COPY quotes.sqlite quotes.sqlite

RUN pip3 --no-cache-dir install -r $requirements

CMD ["fastapi","run", "main.py"]