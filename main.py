# first, some practice code to warm myself up, from http://blog.adnansiddiqi.me/create-your-first-rest-api-in-fastapi/

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Contact(BaseModel):
    contact_id:int
    first_name:str
    last_name:str
    user_name:str
    password:str
 
 
class ContactOut(BaseModel):
    contact_id:int
    first_name:str
    last_name:str
    user_name:str

app = FastAPI(title='Contact.ly', description='APIs for contact Apis', version='0.1')

@app.on_event("startup")
async def startup():
    print("Connecting...")

@app.get("/")
async def root():
    return {"message": "Contact Applications!"}

# @app.get("/")
# def home():
#     return {"Hello": "FastAPI"}
 
# @app.post('/contact', response_model=ContactOut)
# async def create_contact(contact: Contact):
#     return contact

from routers import contact

app = FastAPI(title='Contact.ly', description='APIs for contact Apis', version='0.1')
app.include_router(contact.router_contacts)

