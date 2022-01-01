FROM alpine:latest

ENV USER=yeetbot
ENV UID=38404
ENV GID=48306

RUN apk --no-cache add gcc musl-dev python3 python3-dev curl
RUN addgroup -S yeetbot
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

WORKDIR /home/yeetbot

COPY requirements.txt requirements.txt
COPY yeet_bot_id.py yeet_bot_id.py

RUN python3 -m venv venv
RUN venv/bin/python -m pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

COPY yeet_bot_txt.py yeet_bot_id.py ./

RUN chown -R yeetbot:yeetbot ./
USER yeetbot

EXPOSE 80
CMD venv/bin/python yeet_bot_txt.py