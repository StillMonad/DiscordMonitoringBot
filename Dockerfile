FROM python:3.11
RUN python3 -m venv env
RUN source env/bin/activate
RUN pip install -r requirements.txt
CMD [“python3”, “__main__.py”]
