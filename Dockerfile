FROM python:3.7

ADD main.py /

ADD BaltimoreCyberTrustRoot.crt.pem /

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd 

CMD [ "python", "./main.py" ]