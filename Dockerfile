FROM python:3.7.7-slim

WORKDIR /service

COPY . /service

ENV IP_ADDR_DEVICE_ZK=192.168.20.75
ENV APIREST_ENDPOINT=http://192.168.20.50:9000
ENV TZ=America/Santiago


RUN apt-get update \
    && apt-get -y install iproute2 iputils-ping system-config-printer \
    && pip install --upgrade pip \
    && pip --no-cache-dir install -r requirements.txt

#CMD ["python", "main.py"]
#CMD ["gunicorn"  ,"-b", "0.0.0.0:4000", "wsgi:app"]

CMD ["gunicorn"  ,"--bind", "0.0.0.0:4000", "wsgi:app"]
