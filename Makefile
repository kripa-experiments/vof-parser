.PHONEY: run
run:
	FLASK_ENV=development	pipenv run python nfl-demo.py
