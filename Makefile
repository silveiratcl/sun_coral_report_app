ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose up --build -d --remove-orphans
up:
	docker-compose up -d
down:
	docker-compose down
logs:
	docker-compose logs
migrate:
	docker-compose exec api python manage.py migrate --noinput
makemigrations:
	docker-compose exec api python manage.py makemigrations

superuser:
	docker-compose exec api python manage.py createsuperuser

down-v:
	docker-compose down -v

volume:
	docker volume inspect sun_coral_report_app_postgres_data

shell:
	docker-compose exec api python3 manage.py shell