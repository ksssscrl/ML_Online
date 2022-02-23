FROM python:3.9-slim-bullseye
# RUN mkdir my-model
# ENV MODEL_DIR=/home/jovyan/my-model
ENV MODEL_FILE=model.pkl
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt 

COPY app.py ./app.py
COPY model.pkl ./model.pkl


ENTRYPOINT ["flask","run","--port","5012","--host=0.0.0.0"]