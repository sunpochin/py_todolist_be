from peewee import *
from typing import Any
from .Base import BaseModel

class Contact(BaseModel):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email = CharField(max_length=40)
    phone = CharField(max_length=25)
    status = SmallIntegerField()
    updated_at = DateTimeField()

    class Meta:
        db_table = 'contacts'

async def create_contact(first_name: str, last_name: str, email: str, phone: str, status: int):
    contact_object = Contact(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        status=status
    )
    contact_object.save()
    return contact_object



from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class ContactModel(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
        


