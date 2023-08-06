FROM python:3.9-alpine

ENV TZ="Asia/Jakarta"
ENV HOSTNAME DarkPyro
ENV GIT_PYTHON_REFRESH=quiet

RUN apk add --no-cache \
            git py3-pip

RUN git clone https://github.com/2R-Dark-Kanger-Pro/DarkPyro-REV \
    /app/darkpyro; chmod 777 /app/darkpyro

WORKDIR /app/darkpyro

COPY config.env .

RUN pip3 install -r req*txt

CMD ["python3", "-m", "ProjectDark"]
