# зробив окремим файлом, тому що при створенні міграції не знаходив BASE 

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
