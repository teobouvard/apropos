.PHONY: install runserver website

install:
	pip install --user -r server/requirements.txt
	cd website && npm install

runserver:
	export FLASK_APP=server/routes.py && FLASK_DEBUG=1 && flask run --host 0.0.0.0

website:
	cd website && npm run serve

db:
	mongod --dbpath db_copy