import random
from faker import Faker
from sqlalchemy.orm import Session
from models import Contacts
from db import engine

fake = Faker()

CONTACTS = random.randint(20, 40)

with Session(engine) as session:
    contacts = [
        Contacts(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            mail=fake.unique.email(),
            phone=fake.unique.numerify("+###-###-#######"),
            birthday=fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80),
        )
        for _ in range(CONTACTS)
    ]
    session.add_all(contacts)
    session.commit()

print("Contacts table seeded successfully!")
