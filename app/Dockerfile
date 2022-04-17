FROM python:3.7-buster

RUN apt-get update
RUN apt-get install poppler-utils -y

COPY . /main

WORKDIR /main

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

EXPOSE 8610

CMD [ "run.py" ]