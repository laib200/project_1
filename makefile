



user:
	cd server && python manage.py createsuperuser


makemigrations:
	cd server && python manage.py makemigrations

migrate:makemigrations
	cd server && python manage.py migrate

run:migrate
	cd server && python manage.py runserver 8001 


#________________test_________________
t:
	python test\main.py