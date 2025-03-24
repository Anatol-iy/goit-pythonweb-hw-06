from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url_to_db = "postgresql://postgres:mysecretpassword@localhost:5432/university_db"
engine = create_engine(url_to_db, echo=False)

Session = sessionmaker(bind=engine)
session = Session()