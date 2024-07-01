FROM python:3-alpine

RUN apk update
RUN apk add git
RUN git clone https://github.com/Ignacio687/FakeApiPython_DS2023.git

WORKDIR /FakeApiPython_DS2023
RUN pip install -r requirements.txt
COPY run.py /run.py

ENTRYPOINT ["python3 run.py"]
