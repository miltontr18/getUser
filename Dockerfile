FROM python:3.13-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY getUser.py /app
EXPOSE 5000
VOLUME /app/users_log
CMD ["python3", "getUser.py"]
