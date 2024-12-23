install:
	poetry install

lint:
	flake8 --exclude .git,__pycache__,.mypy_cache,.pytest_cache,.venv,.vscode,txt2musicxml/grammer

format:
	isort .
	black -l 79 .

mypy:
	PYTHONPATH=txt2musicxml MYPYPATH=txt2musicxml mypy txt2musicxml

test:
	PYTHONPATH=txt2musicxml pytest .
	./tests/test_songs.sh

run:
	txt2musicxml < tests/crd_files/la_bamba.crd

build:
	poetry build

publish:
	poetry publish

publish-build:
	poetry publish --build