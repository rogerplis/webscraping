from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


def get_database_connetion():
    return URL.create(
        drivername="postgresql+psycopg2",
        username="dbuser",
        password="dbpassword",
        host="localhost",
        port=5432,
        database="task"
    )


engine = create_engine(get_database_connetion(), echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
