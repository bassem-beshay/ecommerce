web: gunicorn ecommerce.wsgi
release: python manage.py migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('adminbm', 'bassembeshay50@gmail.com', '12345678Aa*') if not User.objects.filter(username='adminbm').exists() else None" | python manage.py shell

