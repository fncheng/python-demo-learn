.PHONY: run

run:
	FLASK_APP=main.py FLASK_ENV=development FLASK_DEBUG=1 flask run --reload --port 3000