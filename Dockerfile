FROM jupyter/scipy-notebook
RUN mkdir my-model
ENV MODEL_DIR=/home/yy240/model.pkl


COPY app.py ./app.py
