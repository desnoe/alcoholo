default: init test

init:
	pip install -r requirements.txt

test:
	nosetests -v tests

.PHONY: init test
