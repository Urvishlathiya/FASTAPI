from sqlalchemy import Column, Integer,Boolean,String,DateTime
from database.database import Base
from datetime import datetime
class Stu(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    F_name = Column(String(20),nullable=False)
    L_name = Column(String(20),nullable=False)
    Course = Column(String(20),nullable=False)
    Mobile_No = Column(String(10),nullable=False)
    Email = Column(String(30),nullable=False)
    Date_of_Birth = Column(String(20),nullable=False)
    Place_of_Birth = Column(String(20),nullable=False)
    Gender = Column(String(20),nullable=False)
    University_name = Column(String(20),nullable=False)
    HSC_Result = Column(String(20),nullable=False)
    HSC_Passing_year = Column(String(20),nullable=False)
    HSC_School_name = Column(String(20),nullable=False)
    Aadhaarcard_num = Column(String(12),nullable=False)
    Father_business = Column(String(20),nullable=False)
    Father_income = Column(String(20),nullable=False)
    Hobbies = Column(String(30),nullable=False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)