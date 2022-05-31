FROM python:3.9.10

WORKDIR /app
COPY . /app
 
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["bash", "start"]
