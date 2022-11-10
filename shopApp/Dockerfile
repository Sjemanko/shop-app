FROM python:3.10.8-slim

ENV PYTHONBUFFERED=1
COPY . /app
WORKDIR /app

RUN python-3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade &&  \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]