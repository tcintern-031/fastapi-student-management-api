from pydantic import BaseModel, Field

class Student(BaseModel):
    id:int = Field(gt=0)
    name:str
    age:int = Field(gt=0, lt=100)