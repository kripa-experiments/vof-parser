.PHONEY: run
run:
	pipenv run gunicorn -b :8080 nfl-demo:app --reload

.PHONEY: run-prod
run-prod:
	pipenv run gunicorn -b :8080 nfl-demo:app

requirements.txt: Pipfile Pipfile.lock
	pipenv lock --requirements > requirements.txt

.PHONEY: deploy
deploy: requirements.txt
	gcloud app deploy app.yaml
