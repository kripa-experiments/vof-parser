.PHONEY: run
run:
	FLASK_ENV=development pipenv run gunicorn -c gunicorn.conf.py -b :8080 nfl-demo:app --reload

.PHONEY: run-reload-templates
run-reload-templates:
	FLASK_ENV=development	pipenv run python nfl-demo.py

.PHONEY: run-prod
run-prod:
	pipenv run gunicorn -c gunicorn.conf.py -b :8080 nfl-demo:app

requirements.txt: Pipfile Pipfile.lock
	pipenv lock --requirements > requirements.txt

.PHONEY: deploy-staging
deploy-staging: requirements.txt
	gcloud app deploy --version staging --no-promote app.yaml
	gcloud app versions start staging

.PHONEY: stop-staging
stop-staging:
	gcloud app versions stop staging

.PHONEY: deploy-prod
deploy-prod: requirements.txt
	gcloud app deploy app.yaml
