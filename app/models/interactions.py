import builtins
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from app.database import Base

class Interaction(Base):
    __tablename__ = 'interactions'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    type = Column(String(50), nullable=True)
    date = Column(Date, nullable=True)
    outcome = Column(Text)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)

    @builtins.property
    def contact(self):
        from sqlalchemy import inspect as _sa_inspect
        _sess = _sa_inspect(self).session
        if _sess is None or self.contact_id is None:
            return None
        from app.models.contacts import Contact
        return _sess.query(Contact).get(self.contact_id)
