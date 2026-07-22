import builtins
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String(255), nullable=True)
    password_hash = Column(String(255), nullable=True)
    @builtins.property
    def contacts(self):
        from sqlalchemy import inspect as _sa_inspect
        _sess = _sa_inspect(self).session
        if _sess is None:
            return []
        from app.models.contacts import Contact
        return _sess.query(Contact).filter(Contact.user_id == self.id).all()

    # Relationships