FROM python:2.7-alpine
RUN apk update && apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install cryptography
RUN pip install werobot
RUN pip install requests
RUN mkdir /script/
COPY entrypoint.sh /script/
# RUN server
CMD ["sh","/script/entrypoint.sh"]