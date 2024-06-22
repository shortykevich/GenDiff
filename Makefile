install:
		poetry install

gendiff:
		poetry run gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

lint:
		poetry run flake8 gendiff

tests-coverage:
		poetry run coverage run -m pytest

format-coverage:
		poetry run coverage lcov -o lcov.info
