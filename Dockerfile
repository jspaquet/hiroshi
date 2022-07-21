FROM python:3.10-alpine

RUN mkdir -p /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --no-cache add bash python3-dev gcc libc-dev libffi-dev

ADD https://github.com/benbjohnson/litestream/releases/download/v0.3.8/litestream-v0.3.8-linux-amd64-static.tar.gz /tmp/litestream.tar.gz
RUN tar -C /usr/local/bin -xzf /tmp/litestream.tar.gz

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install wheel pip-tools
RUN pip-sync

RUN apk --no-cache del python3-dev gcc libc-dev libffi-dev

COPY . .

COPY litestream.yml /etc/litestream.yml

RUN python manage.py collectstatic --noinput

RUN chmod +x /app/entrypoint.sh

EXPOSE 8080

CMD ["/app/entrypoint.sh"]
