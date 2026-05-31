FROM python:3.10
WORKDIR /app
COPY /OSS_fastapi/app /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD python main.py
