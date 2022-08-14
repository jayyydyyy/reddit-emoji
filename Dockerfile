FROM python:3.9

EXPOSE 5000

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD python app.py