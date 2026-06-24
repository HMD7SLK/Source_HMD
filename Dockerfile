FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y ffmpeg
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask

ENV PORT=10000

CMD sh -c "python web.py & python main.py"
