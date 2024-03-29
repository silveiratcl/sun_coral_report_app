FROM python:3.9.2-slim-buster

WORKDIR /app
COPY ./app /app
COPY ./scripts /scripts

LABEL maintainer="silveira.tcl@gmail.com"
LABEL description="Development image for the sun coral GeoDjango API"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean linux-headers
##
RUN apt-get update && apt-get install -y \
    g++ \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev
##
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt


RUN pip install -r requirements.txt

#RUN adduser \
 #   --disabled-password \
  #  --no-create-home \
   # django-user

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    #chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]

#USER django-user
##

#RUN mkdir -p /vol/web/media
#RUN mkdir -p /vol/web/static
#RUN adduser -D user
#RUN chown -R user:user /vol/
#RUN chmod -R 755 /vol/web
#USER user
