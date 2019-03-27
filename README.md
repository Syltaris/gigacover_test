gigacover

# Installation

This project requires `falcon`, `psycopg2`, `sqlalchemy` and `gunicorn` to be installed in a Python 3.6 environment.
At the root of the directory, you can install `pipenv` and run `pipenv install` to easilly setup the files and environment required to run the project.

It also requires a locally hosted PostgreSQL database server to be running with default params.

# Setting up local PostgreSQL DB

Firstly, ensure you have installed PostgreSQL and started up the server instance.
You can follow this guide to setup the instance. https://tableplus.io/blog/2018/10/how-to-start-stop-restart-postgresql-server.html
You then need to setup the default roles required for the database.
Sticking to the default, we shall use a simple `postgres`:`postgres` for a db named `testdb`.

For linux based systems,

```
sudo service postgresql start
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE testdb;"
```

To test if the database is working correctly, you can switch to the postgres user and enter shell into the db instance.

You be able to login to the db by running `sudo -u postgres psql`.
Run `\q` in psql to exit the shell.

# Execution

The backend server is hosted using `gunicorn` by running `gunicorn main:api` in the `./src` directory.
