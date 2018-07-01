.PHONEY: run
run:
	pipenv run gunicorn -b :8080 nfl-demo:app --reload

.PHONEY: run-prod
run-prod:
	pipenv run gunicorn -b :8080 nfl-demo:app
