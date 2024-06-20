from pydantic import BaseModel

class StuBase(BaseModel):
    
    F_name : str
    L_name : str
    Course : str
    Mobile_No : str
    Email : str
    Date_of_Birth : str
    Place_of_Birth : str
    Gender : str
    University_name : str
    HSC_Result : str
    HSC_Passing_year : str
    HSC_School_name : str
    Aadhaarcard_num : str
    Father_business : str
    Father_income : str
    Hobbies : str