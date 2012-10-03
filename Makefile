
test:
	flake8 country_dialcode --ignore=E501,E128
	coverage run --branch --source=country_dialcode `which django-admin.py` test --settings=country_dialcode.test_settings country_dialcode
	coverage report --omit=country_dialcode/test*
