FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    ffmpeg \
    nodejs \
    npm

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=10000

CMD ["python", "main.py"]
