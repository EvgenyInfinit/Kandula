FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /kandula
COPY . /kandula/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=run.py 
ENV FLASK_DEBUG=1

CMD ["/bin/bash", "bin/run"]
