# syntax=docker/dockerfile:1

FROM pytorch/pytorch

RUN apt-get update && \
    apt-get install -y

WORKDIR ./
COPY requirements.txt requirements.txt 
COPY ./src ./

RUN ls
RUN pip install -r requirements.txt
CMD python main.py