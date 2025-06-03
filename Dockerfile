FROM jupyter/base-notebook:latest

USER root
RUN apt update && \
    apt install -y gcc vim git graphviz

COPY requirements.txt /tmp
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

USER $NB_UID