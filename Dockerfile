FROM python:3.9-slim-bullseye

ENV TZ="Asia/Jakarta"

ENV GIT_PYTHON_REFRESH=quiet

RUN apt -y update; apt -y upgrade; \
    apt -y install git

RUN git clone https://github.com/2R-Dark-Kanger-Pro/DarkPyro-REV \
    /app/darkpyro; chmod 777 /app/darkpyro

WORKDIR /app/darkpyro

COPY config.env .

RUN pip install -r req*txt

CMD ["python3", "-m", "ProjectDark"]
