# go to project main directory

# create a python virtual environment

python3 -m venv venv

# activate the virtual environment

windows - .\venv\Scripts\activate
linux - source env/bin/activate

# install required libraries

pip install -r requirement.txt

# django database migration

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

# imports the data from csv file to db

    # run django console

    python3 manage.py shell

    # execute data_migration.py script inside the  shell

    exec(open('data_migrate.py').read())
    ...
    exit()

# run the django server

python3 manage.py runserver



############
* link to api document: https://documenter.getpostman.com/view/9710852/VUjSGjQo

OpenAPI swagger documentation: http://127.0.0.1:8000/swagger/


