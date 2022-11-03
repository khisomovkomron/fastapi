# Project
## Structure
### Folders 

 - alembic - created by alembic init "folder name", used for Database migrations
 - company - side api used in project (example of how to use unrelated project apis)
 - routers - basically all apis are located in this folder (address, auth, todos, users)
### Files

- alembic.ini - alembic configs, where you can set up your database
- database.py - database file to configure your database (postgres) with project
- main.py - main file to run, where all apis from routers folder are imported. This file helps you to run one file to acquire all apis
- models.py - file where all database models are created and held
- requirements.py - file to keep all required libraries for project. 
- Before starting project in command line enter - pip install -r requirements.py



# FastAPI

* pip install fastapi[all] -> install framework with all dependencies

* uvicorn main:app --reload -> start the server and run the project



# FastAPI Routers

* http://127.0.0.1:8000 - code

* http://127.0.0.1:8000/endpoint - handler

* http://127.0.0.1:8000/docs - swagger

* http://127.0.0.1:8000/redoc - another swagger



# ALEMBIC 
* alembic init "folder name" - initializes a new, generic environment

* alembic revision -m "message"  - creates a new revision of the environment

* alembic upgrage "revision #" - run our upgrade migration to our database

* alembic downgrade "revision #" - run out downgrade migration tto our database