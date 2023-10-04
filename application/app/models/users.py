from sqlalchemy import Integer, String, DATE, Column
from models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    dateOfBirth = Column(DATE, nullable=False)
