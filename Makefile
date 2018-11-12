.PHONY: clean-build

clean-build:
	rm -r build dist *.egg-info

release:
	python scripts/make-release.py

test:
	pytest -sv --tap-combined
