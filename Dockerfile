FROM python:3.9-alpine

ENV TZ="Asia/Jakarta"
ENV HOSTNAME DarkPyro
ENV GIT_PYTHON_REFRESH=quiet

RUN apk --no-cache add \
                   git neofetch

RUN git clone https://github.com/2R-Dark-Kanger-Pro/DarkPyro-REV \
    /home/darkpyro

WORKDIR /home/darkpyro

COPY config.env .

RUN pip3 install -r req*txt

CMD ["python3", "-m", "ProjectDark"]
