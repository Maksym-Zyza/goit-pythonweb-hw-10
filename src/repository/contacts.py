from fastapi import HTTPException, status
from src.database.models import Contacts
from datetime import datetime, timedelta
from sqlalchemy.sql import extract


async def search_contacts(first_name, last_name, email, db):
    query = db.query(Contacts)

    if first_name:
        query = query.filter(Contacts.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.filter(Contacts.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.filter(Contacts.email.ilike(f"%{email}%"))

    return query.all()


async def create_contact(body, db):
    contact = Contacts(**body.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def get_contact_by_id(id: int, db):
    contact = db.query(Contacts).filter_by(id=id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


async def update_contact(id: int, body, db):
    contact = db.query(Contacts).filter_by(id=id).first()

    for key, value in body.model_dump().items():
        setattr(contact, key, value)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(id: int, body, db):
    contact = db.query(Contacts).filter_by(id=id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )

    updated_data = body.model_dump()
    for key, value in updated_data.items():
        setattr(contact, key, value)

    db.commit()
    db.refresh(contact)
    return contact


async def delete_contact(id: int, db):
    contact = db.query(Contacts).filter_by(id=id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )

    db.delete(contact)
    db.commit()
    return contact


async def get_upcoming_birthdays(db):
    today = datetime.today().date()
    upcoming = today + timedelta(days=7)

    start_day = today.day
    start_month = today.month
    end_day = upcoming.day
    end_month = upcoming.month

    query = db.query(Contacts)

    if start_month == end_month:
        query = query.filter(
            extract("month", Contacts.birthday) == start_month,
            extract("day", Contacts.birthday) >= start_day,
            extract("day", Contacts.birthday) <= end_day,
        )
    else:
        query = query.filter(
            (
                (extract("month", Contacts.birthday) == start_month)
                & (extract("day", Contacts.birthday) >= start_day)
            )
            | (
                (extract("month", Contacts.birthday) == end_month)
                & (extract("day", Contacts.birthday) <= end_day)
            )
        )

    return query.all()
