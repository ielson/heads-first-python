# Barebone-packages
This is my barebone python package.
It just prints a string when called

It can be installed with `pip install .` or `pip install -e .`.

Tests can be done with `python3 setup.py test`
And code formatting checking with `python3 setup.py flake8`

Versions should be checked at \_\_init__.py

Dists are generated with:
`python3 setup.py sdist`
`python3 setup.py bdist_wheel`

Uploading to test-pypi can be done with:
`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`