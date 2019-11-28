.PHONY: install runserver website

install:
	pip install --user -r requirements.txt

runserver:
	FLASK_APP=server/routes.py && FLASK_DEBUG=1 && flask run

website:
	cd website && npm run serve