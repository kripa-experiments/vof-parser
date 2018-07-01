.PHONEY: run
run:
	FLASK_ENV=development	pipenv run python nfl-demo.py

.PHONEY: run-prod
run-prod:
	pipenv run gunicorn -b :8080 nfl-demo:app
