#requires the installation of packages python, python-dev, postgresql-server-dev-9.4
#and the installation and instanciation of a python virtualenv called venv in the below directory

. ../virgil_venv/venv/bin/activate

pip install flask --upgrade
pip install flask_restful --upgrade
pip install psycopg2 --upgrade
pip install ConfigParser --upgrade
pip install StringGenerator --upgrade
pip install pyjwt --upgrade
