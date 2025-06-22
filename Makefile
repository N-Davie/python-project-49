.PHONY: install build package-install brain-games.PHONY: install brain-games

install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

brain-games:
	uv run brain-games
