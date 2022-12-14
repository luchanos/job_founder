from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class JobBase(BaseModel):
    """shared properties"""
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


class JobCreate(JobBase):
    """this will be used to validate data while creating a Job"""
    title: str
    company: str
    location: str
    description: str


class ShowJob(JobBase):
    """this will be used to format the response to not to have id,owner_id etc"""
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    class Config:
        """to convert non dict obj to json"""
        orm_mode = True
