FROM python:3.10.8-slim

ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade &&  \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

EXPOSE 8000
CMD ["/app/entrypoint.sh"]