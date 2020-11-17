FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY . . 
ENV SQLURI=
ENV SECKEY=
EXPOSE 5000
ENTRYPOINT ["python","app.py"]

