FROM python:3

WORKDIR /usr/src/app

COPY src .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir data
VOLUME data

CMD ["python3", "discord_bot.py"]
