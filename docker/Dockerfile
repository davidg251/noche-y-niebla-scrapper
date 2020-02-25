FROM python:3

ADD . /code

WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "/code/main.py" ]