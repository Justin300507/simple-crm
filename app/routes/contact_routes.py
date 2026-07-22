from typing import Any
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.contacts import Contact
from app.models.notes import Note
from app.models.interactions import Interaction
from app.models.users import User
from app.schemas.contact import ContactCreate, ContactUpdate
from app.schemas.note import NoteCreate
from app.schemas.interaction import InteractionCreate
from app.utils.auth import get_current_user, oauth2_scheme

contact_router = APIRouter()

@contact_router.get("/contacts")
def get_contacts(limit: int = Query(50, ge=1, le=500), offset: int = Query(0, ge=0), db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    return db.query(Contact).filter(Contact.user_id == current_user.id).offset(offset).limit(limit).all()


@contact_router.get("/contacts/search")
def search_contacts(name: str, db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    return db.query(Contact).filter(Contact.user_id == current_user.id, Contact.name.ilike(f'%{name}%')).all()


@contact_router.get("/contacts/{contact_id}")
def get_contact(contact_id: int, db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Not found")
    return contact


@contact_router.post("/contacts", status_code=201)
def create_contact(contact_in: ContactCreate, db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = Contact(**{k: v for k, v in contact_in.dict().items() if k in Contact.__table__.columns.keys() and k not in {'user_id'}}, user_id=current_user.id)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@contact_router.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact_in: ContactUpdate, db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Not found")
    for key, value in contact_in.dict(exclude_unset=True).items():
        setattr(contact, key, value)
    db.commit()
    db.refresh(contact)
    return contact


@contact_router.delete("/contacts/{contact_id}", status_code=204)
def delete_contact(contact_id: int, db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(contact)
    db.commit()


@contact_router.post("/contacts/{contact_id}/notes", status_code=201)
def add_note(contact_id: int, note_in: NoteCreate, db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Not found")
    note = Note(**{k: v for k, v in note_in.dict().items() if k in Note.__table__.columns.keys() and k not in {'contact_id'}}, contact_id=contact.id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@contact_router.get("/contacts/{contact_id}/notes")
def get_notes(contact_id: int, limit: int = Query(50, ge=1, le=500), offset: int = Query(0, ge=0), db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Not found")
    return db.query(Note).filter(Note.contact_id == contact.id).offset(offset).limit(limit).all()


@contact_router.post("/contacts/{contact_id}/interactions", status_code=201)
def log_interaction(contact_id: int, interaction_in: InteractionCreate, db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Not found")
    interaction = Interaction(**{k: v for k, v in interaction_in.dict().items() if k in Interaction.__table__.columns.keys() and k not in {'contact_id'}}, contact_id=contact.id)
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction


@contact_router.get("/contacts/{contact_id}/interactions")
def get_interactions(contact_id: int, limit: int = Query(50, ge=1, le=500), offset: int = Query(0, ge=0), db: Session = Depends(get_db), current_user: Any = Depends(get_current_user)):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Not found")
    return db.query(Interaction).filter(Interaction.contact_id == contact.id).offset(offset).limit(limit).all()
