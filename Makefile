test:
	poetry run pytest tests

lint:
	poetry run flake8

install:
	pip install -r requirements.txt
