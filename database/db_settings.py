DEFAULT_DATABASE_DB = "postgres_alchemy"
DEFAULT_DATABASE_USER = "postgres_alchemy"
DEFAULT_DATABASE_PASSWORD = "XuG76FvNmkuTbf123"
DEFAULT_DATABASE_HOSTNAME = "localhost"
DEFAULT_DATABASE_PORT = 5432

DATABASE_URL = (
    f"postgresql+psycopg2://{DEFAULT_DATABASE_USER}:{DEFAULT_DATABASE_PASSWORD}"
    f"@{DEFAULT_DATABASE_HOSTNAME}:{DEFAULT_DATABASE_PORT}/{DEFAULT_DATABASE_DB}"
                )
