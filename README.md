# sqlalchemy_with_mixin
A sql-alchemy lib with mixin included

This repo includes:
1. SqlAlchemy 2.0.0
2. Docker compose yaml of postgres
3. A sql alchemy mixin for Crud and specific database operations

Install virtualenv library to build virtual environment
```bash
pip install virtualenv
```

Create virtualenv (Make sure you are at root directory of code snippet)
```bash
virtualenv venv
```

Install requirements.txt to virtualenv
```bash
source venv/bin/activate
```

Install requirements.txt to virtualenv
```bash
pip install -r requirements.txt
```

If docker is installed, skip docker install!
Download the Docker quick & easy install script
```bash
 curl -fsSL https://get.docker.com -o get-docker.sh
```
or
```bash
wget -O get-docker.sh https://get.docker.com/
```

Install docker on linux kernel
```bash
sh get-docker.sh
```

Download docker compose
```bash
curl -L "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Test docker-compose
```bash
docker-compose --version
```

Run postgres via command
```bash
docker compose up --build
```

Install alembic 
``` bash
alembic init alembic
```

Run generate for database models
``` bash
alembic revision --autogenerate
```

Upgrade for database models
``` bash
alembic upgrade head
```

Copy env.py at root directory, remove after copy
``` bash
cp -rf env.py alembic/env.py 
```

Copy Database URL to alembic.ini
``` bash
sqlalchemy.url = postgresql+psycopg2://postgres_alchemy:XuG76FvNmkuTbf123@localhost:5432/postgres_alchemy
```
