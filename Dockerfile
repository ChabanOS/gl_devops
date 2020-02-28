FROM python:3.7

WORKDIR /usr/src/app

COPY main.py .

COPY req.txt .

RUN pip install -r req.txt

ENTRYPOINT [ "python", "main.py" ]
