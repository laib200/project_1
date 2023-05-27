#-----[auth]
#     changepassword
user:
	cd server && python manage.py createsuperuser

#--[django]
    # check
    # compilemessages
    # createcachetable
    # dbshell
    # diffsettings
    # dumpdata
    # flush
    # inspectdb
    # loaddata
    # makemessages
makemigrations:
	cd server && python manage.py makemigrations

migrate:makemigrations
	cd server && python manage.py migrate
    # optimizemigration
    # sendtestemail
    # shell
    # showmigrations
    # sqlflush
    # sqlmigrate
    # sqlsequencereset
    # squashmigrations
    # startapp
    # startproject
    # test
    # testserver
run:migrate
	cd server && python manage.py runserver 8001 
# [contenttypes]
#     remove_stale_contenttypes

# [sessions]
#     clearsessions

# [staticfiles]
#     collectstatic
#     findstatic
#     runserver