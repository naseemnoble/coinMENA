# coinMENA
coinMENA is REST API with Python django rest api framework.

## Steps for running

Install virtualenv, It is a tool to create isolated Python environments
```bash
pip install virtualenv
```
Create a virtual environment 'coinMENA_venv' for a project (Python 3.x interpreter used)
```
virtualenv -p /usr/bin/python3 coinMENA_venv
```
Activate virtualenv 'coinMENA_venv'
```
source coinMENA_venv/bin/activate
```
clone project from github
```
git clone https://github.com/naseemnoble/coinMENA.git
```
Change to Project repository directory
```
cd coinMENA
```
Install django and rest api dependencies
```
pip install -r requirements.txt
```
Change to Project root directory
```
cd alphavantage
```
Migrate database
```
python manage.py migrate
```
Run server
```
python manage.py runserver
or
python manage.py runserver 8080 (Change port to 8080)