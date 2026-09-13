FROM python:3.14-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip \
    && rm -rf /usr/local/lib/python3.14/site-packages/pip \
    && rm -rf /usr/local/lib/python3.14/site-packages/pip-*.dist-info

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]