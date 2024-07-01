FROM python:3-alpine

RUN apk update && apk add git
RUN git clone https://github.com/Ignacio687/FakeApiPython_DS2023.git

WORKDIR /FakeApiPython_DS2023
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3", "run.py"]
