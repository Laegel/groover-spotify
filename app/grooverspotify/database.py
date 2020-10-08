import os

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = sqlalchemy.MetaData()

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(
    os.environ.get("POSTGRES_USER"), 
    os.environ.get("POSTGRES_PASSWORD"), 
    "database", # Hostname, "database" in docker-compose context
    5432, # Default port
    os.environ.get("POSTGRES_DB"),
    "prefer"
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)

metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

ModelBase = declarative_base()