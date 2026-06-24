FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    nodejs \
    npm \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "YousefMusic"]
