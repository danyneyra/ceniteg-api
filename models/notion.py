from typing import Optional
from pydantic import BaseModel
from typing import List

class Course(BaseModel):
    code: str
    name: str
    date_start: str
    date_end: Optional[str] | None = ""
    hours: str

class Student(BaseModel):
    name: str
    document: str

class Certificate(BaseModel):
    name: str
    document: str
    course: Course
    date: str
    hash: str
    url: str
