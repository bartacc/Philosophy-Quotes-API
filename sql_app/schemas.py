from pydantic import BaseModel
from typing import List

class Quote(BaseModel):
    id: int
    quote: str
    cited_work: str = None
    author_name: str
    author_bio: str
    author_id: int
    
    class Config:
        orm_mode = True

class QuoteIDs(BaseModel):
    ids: List[int]


class Author(BaseModel):
    id: int
    author_name: str
    author_bio: str
    quote_ids: List[int]

    class Config:
        orm_mode = True






