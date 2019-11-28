install:
	pip install --user -r requirements.txt

runserver:
	cd server && flask run