FROM python:3.11.4
RUN pip install -r requirements.txt
CMD [“python3”, “__main__.py”]
