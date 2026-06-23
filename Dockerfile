FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y \
    ffmpeg git curl \
    build-essential \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libpng-dev \
    libwebp-dev \
    && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "YousefMusic"]
