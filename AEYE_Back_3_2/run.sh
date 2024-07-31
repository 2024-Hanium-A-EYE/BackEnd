run_server()
{
  python manage.py makemigrations \
  && python manage.py migrate \
  && python manage.py runserver 127.0.0.1:6000
}
