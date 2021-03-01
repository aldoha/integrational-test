
base integrational sign up scenario with [POST /accounts](http://lifeserver-staging.tocaboca.com/public-api-doc?v=3#accounts_post) and [POST /accounts/authentication](http://lifeserver-staging.tocaboca.com/public-api-doc?v=3#accounts_authentication_post) methods

#### Dependencies
* `pytest` to run test
* `requests` to handle http requests
* `pyjwt` to parse jwt-tokens
* `blahblah` and `district42` to generate fake data for requests

#### Setup environment
```
$ python3 -m venv .venv
$ .venv/bin/pip3 install -r requirements.txt
```

#### Run test
```
$ .venv/bin/pytest -v test.py
```