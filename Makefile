PROJECT_NAME = BruteSniffing_Fisher

PYTHON = python

.PHONY: tests
tests:  $(info $(M) testing package...)
	@pip install pytest > /dev/null
	@python -m pytest tests

.PHONY: coverage
coverage: $(info $(M) coverage testing package...)  ## test coverage package
	pip install pytest pytest-cov > /dev/null
	python -m pytest tests --cov=$(PROJECT_NAME) --cov-fail-under=0