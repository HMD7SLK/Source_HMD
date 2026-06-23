FROM python:3.10-bullseye

RUN apt-get update && \
    apt-get install -y ffmpeg git curl && \
    apt-get clean

COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD bash start
