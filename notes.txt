# pip install fastapi[all] -> install framework with all dependicies
# uvicorn book:app --reload -> start the server and run the project

# http://127.0.0.1:8000 - code
# http://127.0.0.1:8000/docs - swagger
# http://127.0.0.1:8000/redoc - another swagger

# alembic init <folder name> - initializes a new, generic environment
# alembic revision -m <message>  - creates a new revision of the environment
# alembic upgrage <revision #> - run our upgrade migration to our database
# alembic downgrade <revision #> - run out downgrade migration tto our database