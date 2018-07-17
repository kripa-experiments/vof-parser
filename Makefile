
init:
	pipenv install --ignore-pipfile

run:
	FLASK_ENV=development pipenv run gunicorn -c gunicorn.conf.py -b :8080 nfl-demo:app --reload

run-local-ssl:
	FLASK_ENV=development	pipenv run python nfl-demo.py

run-prod:
	pipenv run gunicorn -c gunicorn.conf.py -b :8080 nfl-demo:app

requirements.txt: Pipfile Pipfile.lock
	pipenv lock --requirements > requirements.txt

deploy-staging: requirements.txt
	gcloud app deploy --version staging --no-promote app.yaml
	gcloud app versions start staging

stop-staging:
	gcloud app versions stop staging

deploy-prod: requirements.txt
	gcloud app deploy app.yaml

.PHONEY: run deploy-prod stop-staging deploy-staging run-prod run-reload-templates
