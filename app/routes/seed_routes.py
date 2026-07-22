from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User
from app.models.contacts import Contact
from app.models.notes import Note
from app.models.interactions import Interaction

seed_router = APIRouter()

@seed_router.post("/seed")
def seed_data(db: Session = Depends(get_db)):
    # Seed Users
    users = [
        User(email="alex.chen@example.com", password_hash="hashed_password_1"),
        User(email="maria.garcia@example.com", password_hash="hashed_password_2"),
        User(email="james.kim@example.com", password_hash="hashed_password_3"),
        User(email="linda.smith@example.com", password_hash="hashed_password_4"),
        User(email="john.doe@example.com", password_hash="hashed_password_5")
    ]
    for user in users:
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
        except IntegrityError:
            db.rollback()  # Skip if user already exists

    # Seed Contacts
    contacts = [
        Contact(name="Alex Chen", email="alex.chen@example.com", phone="123-456-7890", company="Tech Co", status="Lead"),
        Contact(name="Maria Garcia", email="maria.garcia@example.com", phone="234-567-8901", company="Health Inc", status="Prospect"),
        Contact(name="James Kim", email="james.kim@example.com", phone="345-678-9012", company="Finance LLC", status="Customer"),
        Contact(name="Linda Smith", email="linda.smith@example.com", phone="456-789-0123", company="Retail Corp", status="Churned"),
        Contact(name="John Doe", email="john.doe@example.com", phone="567-890-1234", company="Service Co", status="Lead")
    ]
    for contact in contacts:
        try:
            db.add(contact)
            db.commit()
            db.refresh(contact)
        except IntegrityError:
            db.rollback()  # Skip if contact already exists

    # Seed Notes
    notes = [
        Note(content="Follow up with Alex Chen", contact_id=1),
        Note(content="Meeting scheduled with Maria Garcia", contact_id=2),
        Note(content="Send proposal to James Kim", contact_id=3),
        Note(content="Check in with Linda Smith", contact_id=4),
        Note(content="Discuss project with John Doe", contact_id=5)
    ]
    for note in notes:
        try:
            db.add(note)
            db.commit()
            db.refresh(note)
        except IntegrityError:
            db.rollback()  # Skip if note already exists

    # Seed Interactions
    interactions = [
        Interaction(type="Call", contact_id=1),
        Interaction(type="Email", contact_id=2),
        Interaction(type="Meeting", contact_id=3),
        Interaction(type="Call", contact_id=4),
        Interaction(type="Email", contact_id=5)
    ]
    for interaction in interactions:
        try:
            db.add(interaction)
            db.commit()
            db.refresh(interaction)
        except IntegrityError:
            db.rollback()  # Skip if interaction already exists

    return {"message": "Database seeded successfully"}