FROM python:3.7-alpine
WORKDIR /app
COPY ./main.py /app
COPY ./instalables.txt /app
RUN pip install -r instalables.txt
CMD ["python","main.py"]