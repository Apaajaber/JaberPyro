FROM python:3.9-slim-bullseye

ENV TZ="Asia/Jakarta"

ENV GIT_PYTHON_REFRESH=quiet

<<<<<<< HEAD
RUN apk --no-cache add \
                   git neofetch
=======
RUN apt -y update; apt -y upgrade; \
    apt -y install git
>>>>>>> parent of 84aa04d (same: base os docker)

RUN git clone https://github.com/2R-Dark-Kanger-Pro/DarkPyro-REV \
    /home/darkpyro

WORKDIR /home/darkpyro

COPY config.env .

RUN pip3 install -r req*txt

CMD ["python3", "-m", "ProjectDark"]
