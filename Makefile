# Makefile

VIRTUALENV = venv/
PRETTIER = ./static/node_modules/.bin/prettier

launch:
	. $(VIRTUALENV)bin/activate; python3.5 manage.py runserver

install: create_virtualenv pip_install

create_virtualenv:
	if [ ! -d env ]; then virtualenv -p /usr/bin/python3.5 $(VIRTUALENV); fi

pip_install:
	. $(VIRTUALENV)bin/activate; pip3.5 install -r requirements.txt

pretty:
	$(PRETTIER) --single-quote --no-semi --write "src/**/*.js"