from fastapi import FastAPI, HTTPException, APIRouter , Depends ,Header
from database.database import SessionLocal
from src.models.stud import Stu
from src.schemas.user import StuBase
from src.utils.token import get_token,decode_token_uname,decode_token_user_email,decode_token_user_id
#from src.schemas.student import RollStu, BranchStu
User1 = APIRouter()
db = SessionLocal()


@User1.post("/student/", response_model=StuBase)
def create_student(stu: StuBase):
    newStudent = Stu(

    F_name = stu.F_name,
    L_name = stu.L_name,
    Course = stu.Course,
    Mobile_No = stu.Mobile_No,
    Email = stu.Email,
    Date_of_Birth =stu.Date_of_Birth,
    Place_of_Birth = stu.Place_of_Birth,
    Gender = stu.Gender,
    University_name = stu.University_name,
    HSC_Result =stu.HSC_Result,
    HSC_Passing_year = stu.HSC_Passing_year,
    HSC_School_name = stu.HSC_School_name,
    Aadhaarcard_num = stu.Aadhaarcard_num,
    Father_business = stu.Father_business,
    Father_income = stu.Father_income,
    Hobbies =stu.Hobbies
    )
    db.add(newStudent)
    db.commit()
    return stu



@User1.get("/get_student_details", response_model=StuBase)
def read_person(student_id = Depends(decode_token_user_id)):
    
    stu = db.query(Stu).filter(Stu.id == student_id, Stu.is_active==True , Stu.is_deleted == False).first()
    if stu is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return stu



@User1.get("/post_student_details/", response_model=list[StuBase])
def all_persons():
    stu = db.query(Stu).filter(Stu.is_active==True , Stu.is_deleted==False).all()
    length_list = len(stu)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return stu



@User1.put("/Update_student_details/", response_model=StuBase)
def update_person(student_id: int, stu: StuBase):
    db_stu = db.query(Stu).filter(Stu.id == student_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db_stu.F_name = stu.F_name,
    db_stu.L_name = stu.L_name,
    db_stu.Course = stu.Course,
    db_stu.Mobile_No = stu.Mobile_No,
    db_stu.Email = stu.Email,
    db_stu.Date_of_Birth =stu.Date_of_Birth,
    db_stu.Place_of_Birth = stu.Place_of_Birth,
    db_stu.Gender = stu.Gender,
    db_stu.University_name = stu.University_name,
    db_stu.HSC_Result =stu.HSC_Result,
    db_stu.HSC_Passing_year = stu.HSC_Passing_year,
    db_stu.HSC_School_name = stu.HSC_School_name,
    db_stu.Aadhaarcard_num = stu.Aadhaarcard_num,
    db_stu.Father_business = stu.Father_business,
    db_stu.Father_income = stu.Father_income,
    db_stu.Hobbies =stu.Hobbies
    db.commit()
    
    return db_stu




@User1.delete("/delete_student")
def delete_person(student_id = Depends(decode_token_user_id)):
    
    db_stu = db.query(Stu).filter(Stu.id == student_id).first()
    if db_stu is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_stu)
    db.commit()
    return {"message": "Student deleted successfully"}


#this code for encode the detail or create token
@User1.get("/get_token")
def get_detail(id:str,Email: str, uname :str):

    access_token = get_token(id,Email,uname)

    return access_token


@User1.get("/get_email")
def get_email_decode(token:str = Header(...)):

    email_deco = decode_token_user_email(token)

    return email_deco

