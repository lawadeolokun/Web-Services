FROM python:3.10

WORKDIR /app

RUN apt update && apt install -y git

RUN git clone https://github.com/lawadeolokun/Web-Services.git

WORKDIR /app/Web-Services

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]