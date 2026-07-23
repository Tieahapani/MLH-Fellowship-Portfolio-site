FROM python:3.9-slim-buster

COPY requirements.txt /myportfolio/requirements.txt

WORKDIR /myportfolio

RUN pip3 install -r requirements.txt

COPY . /myportfolio

CMD flask run --host=0.0.0.0

EXPOSE 5000
