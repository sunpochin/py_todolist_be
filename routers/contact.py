from fastapi import APIRouter

router_contacts = APIRouter(
    prefix="/contacts",
    tags=["contacts"]
)

@router_contacts.get("/",summary="List of contacts", description="Returns all contacts" )
async def get_contacts():
    #create(first_name='Addu', last_name='Pagal', email='addu@gmail.com', phone='123-494', status=1)
    return [{'status': 'OK'}]



@router_contacts.get("/view/{id}", summary="Returns a single contact")
async def view(id: int):
    """
        Haha this is awesome! To view all details related to a single contact

        - **id**: The integer id of the contact you want to view details.
    """
    return [{'status': 'OK'}]
    

from models.contact import create_contact

@router_contacts.post("/", summary="Create a new contact")
async def create(first_name: str, last_name: str, email: str, phone: str, status: int):
    return await create_contact(first_name=first_name, last_name=last_name, email=email, phone=phone, status=status)

    