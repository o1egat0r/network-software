.PHONY: test verify-docker up config

# test: pytest only (no Docker).
# verify-docker: compose + lab10 image (needs Docker).
test:
	python -m pytest tests -q

verify-docker:
	docker compose config -q
	docker build -t devices-s05-local -f labs/week-10/Dockerfile labs/week-10

up:
	docker compose up --build

config:
	docker compose config
