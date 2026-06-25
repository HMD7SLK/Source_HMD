FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y ffmpeg curl
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
