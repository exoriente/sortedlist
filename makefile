all: nice pytest

nice: format mypy

format: black ruff

black:
	black .

ruff:
	ruff --fix .

mypy:
	mypy .

pytest:
	pytest --cov

coverage: pytest
	coverage html
	open htmlcov/index.html

tox:
	tox -p
