FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv
RUN python3 -m venv .venv

WORKDIR /code

COPY requirements.txt /code/
RUN /.venv/bin/pip install -r requirements.txt

COPY . /code/
EXPOSE 8000
RUN chmod +x /code/start.sh
ENTRYPOINT ["./start.sh"]
