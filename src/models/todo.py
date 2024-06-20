from sqlalchemy import Column, Integer, String
from database.database import Base
class Stu(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    to_do_name = Column(String)
    to_do_title = Column(String)
    to_do_description = Column(String)
    