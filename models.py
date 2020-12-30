from sqlalchemy import Column, Integer, String, Text

#from db import Base
from app import db

class Link(db.Base):
    __tablename__ = 'Link'
    id = Column(String(length=50), primary_key=True)
    url = Column(Text(), nullable=False)

    @classmethod
    def insert_url(cls, id, url):
        new_url = cls(id=id, url=url)

        db.session.add(new_url)
        db.session.commit()
    
    @classmethod 
    def get_url_by_id(cls, url_id):
        url = db.session.query(cls).filter_by(id=url_id).first()

        return url

