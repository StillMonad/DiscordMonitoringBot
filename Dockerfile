FROM python:3.11.4
COPY . /DiscordMonitoringBot
RUN cd /DiscordMonitoringBot && pip install -r requirements.txt
CMD ["python3", "__main__.py"]
