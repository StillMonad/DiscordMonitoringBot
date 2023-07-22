FROM 3.11.4-alpine3.18
RUN pip install -r requirements.txt
CMD [“python3”, “__main__.py”]
