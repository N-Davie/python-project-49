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
	uv run brain-even


brain-calc:
	uv run brain-calc


brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression


brain-prime:
	uv run brain-prime

lint:
	uv run ruff check brain_games
