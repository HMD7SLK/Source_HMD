FROM python:3.10-bullseye

RUN apt-get update && \
    apt-get install -y ffmpeg git curl && \
    apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -U pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "YousefMusic"]
