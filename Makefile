.PHONY: install build package-install brain-games

install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

brain-games:
	uv run brain-games

brain-even:
	poetry run brain-even


brain-calc:
	poetry run brain-calc


brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression


brain-prime:
	poetry run brain-prime

lint:
	uv run ruff check brain_games
