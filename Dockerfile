FROM python:3.10-bullseye

RUN apt-get update && \
    apt-get install -y ffmpeg git curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["python3", "-m", "YousefMusic"]
