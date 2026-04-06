APP_ENV ?= uat
PORT ?= 8001

run:
	APP_ENV=$(APP_ENV) uv run fastapi dev app/main.py --port $(PORT)
