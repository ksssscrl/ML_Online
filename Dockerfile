FROM python:3.9-slim-bullseye
RUN mkdir my-model
ENV MODEL_FILE=model.pkl



COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt 

COPY app.py ./app.py
