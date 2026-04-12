FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY nestra.py config.py boot.sh ./

RUN chmod +x boot.sh

ENV FLASK_APP=nestra.py

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]