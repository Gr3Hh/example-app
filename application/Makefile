service ?= app
flag ?= -d
params ?=
shell ?= bash

up:
	docker-compose up $(flag)

build_up:
	docker-compose up $(flag) --build

stop:
	docker-compose stop

logs:
	docker-compose logs -f $(service)

shell:
	docker-compose run --rm $(service) $(shell)

lint:
	poetry run flake8 ./app
	poetry run bandit -r -c pyproject.toml ./app

migrate:
	docker-compose run --rm app alembic upgrade head

makemigration:
	docker-compose run --rm app alembic revision --autogenerate -m "$(msg)"

rollback:
	docker-compose run --rm app alembic downgrade -1