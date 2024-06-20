from fastapi import FastAPI, HTTPException, APIRouter
from database.database import SessionLocal
from src.models.todo import Stu
from src.schemas.todo import StuBase
#from src.schemas.student import RollStu, BranchStu
Todo1 = APIRouter()
db = SessionLocal()


@Todo1.post("/todo/", response_model=StuBase)
def create_student(stu: StuBase):
    newStudent = Stu(
        to_do_name=stu.to_do_name,
        to_do_title =stu.to_do_title,
        to_do_description =stu.to_do_description,
    )
    db.add(newStudent)
    db.commit()
    return stu
@Todo1.get("/todo/{todo_id}", response_model=StuBase)
def read_person(todo_id: int):
    stu = db.query(Stu).filter(Stu.id == todo_id).first()
    if stu is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return stu
@Todo1.get("/todo/", response_model=list[StuBase])
def read_persons():
    stu = db.query(Stu).all()
    length_list = len(stu)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return stu
@Todo1.put("/todo/{todo_id}", response_model=StuBase)
def update_person(todo_id: int, stu: StuBase):
    db_stu = db.query(Stu).filter(Stu.id == todo_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db_stu.to_do_name = stu.to_do_name
    db_stu.to_do_title = stu.to_do_title
    db_stu.to_do_description = stu.to_do_description
    db.commit()
    
    return db_stu
@Todo1.delete("/todo/{todo_id}")
def delete_person(todo_id: int):
    db_stu = db.query(Stu).filter(Stu.id == todo_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_stu)
    db.commit()
    return {"message": "Student deleted successfully"}
