import builtins
from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class Contact(Base):
    __tablename__ = 'contacts'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=True)
    email = Column(String(255))
    phone = Column(String(50))
    company = Column(String(255))
    status = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    @builtins.property
    def interactions(self):
        from sqlalchemy import inspect as _sa_inspect
        _sess = _sa_inspect(self).session
        if _sess is None:
            return []
        from app.models.interactions import Interaction
        return _sess.query(Interaction).filter(Interaction.contact_id == self.id).all()

    @builtins.property
    def notes(self):
        from sqlalchemy import inspect as _sa_inspect
        _sess = _sa_inspect(self).session
        if _sess is None:
            return []
        from app.models.notes import Note
        return _sess.query(Note).filter(Note.contact_id == self.id).all()

    @builtins.property
    def user(self):
        from sqlalchemy import inspect as _sa_inspect
        _sess = _sa_inspect(self).session
        if _sess is None or self.user_id is None:
            return None
        from app.models.users import User
        return _sess.query(User).get(self.user_id)
