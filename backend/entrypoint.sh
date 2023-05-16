#!/bin/sh
echo $DATABASE
# if [ "$DATABASE" = "mysql" ]
if [ "$DB_ENGINE" = "django.db.backends.mysql" ]
then
    echo "Waiting for mysql..."
    
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
    
    echo "MySQL started"
fi

nc -zv $DB_HOST $DB_PORT

# python manage.py collectstatic --noinput

# mysql -u $MYSQL_USER -e "create database $MYSQL_DB";

python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo "from django.contrib.auth.models import User;
User.objects.filter(email='$DJANGO_ADMIN_EMAIL').delete();
User.objects.create_superuser('$DJANGO_ADMIN_USER', '$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_PASSWORD')" | python manage.py shell
# echo "from django.contrib.auth import get_user_model; 
# User = get_user_model(); 
# User.objects.filter(email='$DJANGO_ADMIN_EMAIL').delete();
# User.objects.create_superuser('$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_USER', '$DJANGO_ADMIN_FIRST_NAME', '$DJANGO_ADMIN_PASSWORD')" | python manage.py shell

exec "$@"