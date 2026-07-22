from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.contacts import Contact
from sqlalchemy import func

stats_router = APIRouter()

@stats_router.get('/stats/pipeline')
def get_pipeline_stats(db: Session = Depends(get_db)):
    lead_count = db.query(func.count(Contact.id)).filter(Contact.status == 'Lead').scalar()
    prospect_count = db.query(func.count(Contact.id)).filter(Contact.status == 'Prospect').scalar()
    customer_count = db.query(func.count(Contact.id)).filter(Contact.status == 'Customer').scalar()
    churned_count = db.query(func.count(Contact.id)).filter(Contact.status == 'Churned').scalar()

    return {
        'lead_count': lead_count,
        'prospect_count': prospect_count,
        'customer_count': customer_count,
        'churned_count': churned_count
    }