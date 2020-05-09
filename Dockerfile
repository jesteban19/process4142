FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD /shop_book/ .
RUN pip install -r requirements.txt