python3 makeconf.py > /geekpie/geekpie/geekpie/CONFIG.py

cd geekpie

# python3 manage.py createcachetable
python3 manage.py makemigrations
python3 manage.py migrate

nohup gunicorn geekpie.wsgi:application -b 127.0.0.1:8080 --workers 4 --worker-connections 65535&
service nginx start

while true
do
    sleep 1
done
