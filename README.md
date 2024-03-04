# Project Setup

Project Setup instructions

virtualenv venv
source venv/bin/activate

pip install poetry
make install
make migrations
make migrate

<!-- read Makefile for more commands -->

mkdir -p local
cp core/core/settings/templates/settings.dev.py ./local/settings.dev.py

<!-- optional -->
<!-- if you don't want to create new db or user add your db data in ./local/settings.dev.py -->

sudo -u postgres psql
CREATE DATABASE smptlib_task_db;
CREATE USER db_user WITH PASSWORD '123456789';
ALTER DATABASE smptlib_task_db owner to db_user ;
GRANT ALL PRIVILEGES ON DATABASE smptlib_task_db TO db_user ;

<!-- add your Gmail account data in ./local/settings.dev.py -->
<!-- note that your google account should have 2 step-verification and app password -->

EMAIL_ACCOUNT = ""
EMAIL_PASSWORD = ""
