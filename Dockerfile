FROM python:3.11-alpine

RUN apk update && apk add git
RUN git clone https://github.com/Ignacio687/FakeApiPython_DS2023.git

WORKDIR /FakeApiPython_DS2023
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
