# REST API CRUD with fastapi and postgres

## Pre-requisite

- Must have install `python 3.10+`
- Install `uv` from [here](https://docs.astral.sh/uv/getting-started/installation/) ,if it is not installed in your machine.
- Either use Postgress in docker or install it 

## Tech used

- Uv for creating the project and managing dependencies
- Python 3.12
- FastApi
- SqlAlchemy
- Alembic
- PostgreSQL

# How to run a project

- Create a database with name `book_db`
- Clone the repository `git clone https://github.com/rd003/fastapi_postgres_crud.git`
- Open it in terminal `cd fastapi_postgres_crud`

Fire these commands (they may vary to windows): 

- `touch .env` (create a file, this command won't work in windows powershell/command prompt)
-  Open the `.env` file (in linux/mac you may use `vim .env` or nano .env) and paste the content below

```env
DEBUG=True
DATABASE_URL=postgresql://postgres:p%4055w0rd@localhost:5432/book_db
```
Replace DATABASE_URL with yours.

- uv venv` (will create a virtual environment)
- `source .venv/bin/activate` (will activate venv)
- `uv sync`  (to install the dependencies)
- `alembic upgrade head` (will create tables in the database)
- Run project with `uvicorn src.main:app --reload`. Bydefault, the app will be listening at `http://127.0.0.1:8000`
- In the web browser, open this url `http://127.0.0.1:8000/docs`. It will open the `swagger ui`

