from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)


class Contacts(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    birthday = Column(DateTime, nullable=True)
