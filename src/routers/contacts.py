from fastapi import APIRouter, Depends, Query, status
from src.database.db import get_db
from src.repository import contacts as repository
from src.schemas import contacts as schemas
from typing import Optional

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", name="List of contacts")
async def get_contacts(
    first_name: Optional[str] = Query(None),
    last_name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    db=Depends(get_db),
):
    contacts = await repository.search_contacts(first_name, last_name, email, db)
    return contacts


@router.post(
    "/", response_model=schemas.ContactResponse, status_code=status.HTTP_201_CREATED
)
async def create_contact(body: schemas.ContactModelRegister, db=Depends(get_db)):
    contact = await repository.create_contact(body, db)
    return contact


@router.get("/birthdays", name="Upcoming birthdays (7 days)")
async def get_upcoming_birthdays(db=Depends(get_db)):
    contacts = await repository.get_upcoming_birthdays(db)
    return contacts


@router.get("/{id}", name="Get contact by id")
async def get_contact_by_id(id: int, db=Depends(get_db)):
    contact = await repository.get_contact_by_id(id, db)
    return contact


@router.put(
    "/{id}", name="Update contact by id", response_model=schemas.ContactResponse
)
async def update_contact(
    id: int, body: schemas.ContactModelRegister, db=Depends(get_db)
):
    contact = await repository.update_contact(id, body, db)
    return contact


@router.delete(
    "/{id}", name="Delete contact by id", response_model=schemas.ContactResponse
)
async def delete_contact(id: int, db=Depends(get_db)):
    contact = await repository.delete_contact(id, db)
    return contact
