FROM python:3.10

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY ./templates /app/templates/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]