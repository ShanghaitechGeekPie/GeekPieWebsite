FROM django:1.8.6-python3

MAINTAINER eastpiger @ Geek Pie Association

EXPOSE 80

RUN apt-get update && apt-get install nginx libjpeg-dev -y
RUN pip3 install mysqlclient gunicorn django-cms djangocms-text-ckeditor Markdown

RUN mkdir /logs
RUN mkdir /geekpie
WORKDIR /geekpie
COPY . /geekpie
COPY geekpie.conf /etc/nginx/sites-enabled/geekpie.conf
RUN chmod +x ./loader.sh

CMD ./loader.sh
