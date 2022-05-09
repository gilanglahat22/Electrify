from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.config import *

engine = create_engine(f"mariadb+mariadbconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}")

__Session = sessionmaker()
__Session.configure(bind=engine)

Session = __Session()
