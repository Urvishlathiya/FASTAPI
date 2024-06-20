from pydantic import BaseModel

class StuBase(BaseModel):
    to_do_name : str
    to_do_title: str
    to_do_description : str