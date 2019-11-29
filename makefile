.PHONY: install runserver website

install:
	pip install --user -r server/requirements.txt
	cd website && npm install

runserver:
	export FLASK_APP=server/routes.py && FLASK_DEBUG=1 && flask run

website:
	cd website && npm run serve