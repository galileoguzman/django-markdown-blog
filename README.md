# django-markdown-blog


This is an implementation of markdown inside django app as blog. Implemented in the admin as form and in the templates.

The site was built with:

    Django==1.11.7
    django-autoslug==1.9.3
    django-markdown-deux==1.0.5
    django-pagedown==0.1.3
    Markdown==2.6.9
    markdown2==2.3.5
    pytz==2017.3

To run the project you have to have installed:

		Virtualenv
		python 2.7 || python 3


To run the project follow the next steps

- Create a virtualenv named .venv inside the repository (don't worry we're ignoring)

		virtualenv .venv

- After that init the virtual env

		source .venv/bin/activate

- Now you have to run the migrations, create a super user and run the dev server

		./manage.py migrate
		./manage.py createsuperuser
		./manage.py runserver

**Right now the project is set up for add the post via Django Admin.**
