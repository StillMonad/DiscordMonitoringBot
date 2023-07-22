FROM python:3.11.4
COPY . /DiscordMonitoringBot
WORKDIR /DiscordMonitoringBot
RUN pip install -r requirements.txt
CMD ["python3", "__main__.py"]
