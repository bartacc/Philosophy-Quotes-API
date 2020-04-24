from sqlalchemy.orm import Session
from . import models, schemas

from typing import List, Set

import random

def get_quote(db: Session, quote_id: int):
    quote = db.query(models.Quote).filter(models.Quote.id == quote_id).first()
    if quote is None:
        return None
    data = schemas.Quote(id = quote.id, quote=quote.quote, cited_work=quote.cited_work, author_name=quote.author_name, author_bio=quote.author.info, author_id=quote.author.id)
    return data

def get_author(db: Session, author_id: int):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author is None:
        return None
    quote_ids = [quote.id for quote in author.quotes]
    data = schemas.Author(id=author_id, author_name=author.name, author_bio=author.info, quote_ids=quote_ids)
    return data

def get_image(db: Session, author_id: int):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author is None:
        return None
    return author.image

def list_quote_ids(db: Session):
    quotes = db.query(models.Quote).all()
    ids = [quote.id for quote in quotes]
    return ids

def get_random_quote(db: Session):
    ids = list_quote_ids(db)
    random_id = random.choice(ids)
    
    return get_quote(db, random_id)





