from pydantic import BaseModel, EmailStr, constr
from datetime import date


class ContactModelRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date


class ContactResponse(ContactModelRegister):
    id: int
