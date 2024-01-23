.PHONY: default dev start install

default: dev

dev:
	@dotenv venv/bin/python __main__.py
start:
	@venv/bin/python __main__.py
install:
	@python -m venv venv && venv/bin/python -m pip install -r requirements.txt
