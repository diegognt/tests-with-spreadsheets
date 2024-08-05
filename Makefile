all-tests:
	@docker compose run --rm python -m unittest discover -s tests

arithmetic-test:
	@docker compose run --rm python -m unittest ./tests/test_arithmetic_lib.py
