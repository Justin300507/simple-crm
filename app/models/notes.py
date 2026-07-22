import builtins
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from app.database import Base
from sqlalchemy.sql import func

class Note(Base):
    __tablename__ = 'notes'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    content = Column(Text, nullable=True)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)

    @builtins.property
    def contact(self):
        from sqlalchemy import inspect as _sa_inspect
        _sess = _sa_inspect(self).session
        if _sess is None or self.contact_id is None:
            return None
        from app.models.contacts import Contact
        return _sess.query(Contact).get(self.contact_id)
