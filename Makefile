default: init test

init:
	pip install -r requirements.txt

test:
	nosetests -v tests --with-coverage --cover-package=alcoholo

.PHONY: init test
