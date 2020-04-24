from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey

from sqlalchemy.orm import relationship
from .database import Base

class Quote(Base):
    __tablename__ = 'Quotes'
    id = Column('ID', Integer, primary_key=True, index=True)
    quote = Column('Quote', String, unique=True, index=True)
    cited_work = Column('Cited_Work', String)

    author_name = Column('Author', ForeignKey('Authors.Name'))

    author = relationship('Author', back_populates='quotes')


class Author(Base):
    __tablename__ = 'Authors'
    id = Column('ID', Integer, primary_key=True, index=True)
    name = Column('Name', String, unique=True, index=True)
    info = Column('Info', String)
    image = Column('Image', LargeBinary)

    quotes = relationship('Quote', order_by=Quote.id, back_populates='author')
