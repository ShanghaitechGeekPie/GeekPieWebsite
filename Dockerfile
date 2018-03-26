FROM django:1.8.6-python3

MAINTAINER eastpiger @ Geek Pie Association

EXPOSE 80

RUN apt-get update && apt-get install gcc python-dev zlib1g-dev nginx libjpeg-dev python3-pil -y
RUN pip3 install mysqlclient gunicorn django-cms djangocms-text-ckeditor Markdown

RUN mkdir /logs
RUN mkdir /geekpie
WORKDIR /geekpie
COPY . /geekpie
COPY geekpie.conf /etc/nginx/sites-enabled/geekpie.conf
COPY nginx.conf /etc/nginx/nginx.conf
RUN chmod +x ./loader.sh

CMD ./loader.sh
