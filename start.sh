source venv/bin/activate
ifconfig | grep "inet "
sleep 2
# python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:80