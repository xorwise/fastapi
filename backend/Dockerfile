FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./wait-for /code/wait-for
COPY ./docker_scripts /code/docker_scripts

RUN chmod a+x docker_scripts/*.sh
RUN chmod a+x wait-for
