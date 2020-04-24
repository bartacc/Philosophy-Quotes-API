from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import Response
from sql_app import schemas, crud, database
from sqlalchemy.orm import Session

from typing import Set, List

app = FastAPI()


@app.get('/randomQuote', response_model = schemas.Quote)
def get_random_quote(db: Session = Depends(database.get_db)):
    return crud.get_random_quote(db)

@app.get('/listQuoteIDs', response_model = schemas.QuoteIDs)
def list_quote_ids(db: Session = Depends(database.get_db)):
    ids = crud.list_quote_ids(db)
    return {'ids': ids}

@app.get('/quote/{quote_id}', response_model = schemas.Quote)
def get_quote(quote_id: int, db: Session = Depends(database.get_db)):
    quote = crud.get_quote(db, quote_id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

@app.get('/author/{author_id}', response_model = schemas.Author)
def get_author(author_id: int, db: Session = Depends(database.get_db)):
    author = crud.get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@app.get('/image/{author_id}', response_class = Response)
def get_image(author_id: int, db: Session = Depends(database.get_db)):
    image = crud.get_image(db, author_id)
    if image is None:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(content=image, media_type='image/jpeg')