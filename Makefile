init:
	pip install pipenv
	pipenv install

test:
	pipenv run pytest tests
