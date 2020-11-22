# An API that gives you some nice philosopher quotes.

## To run:

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

uvicorn main:app or ~/.local/bin/uvicorn main:app


# Paths:

/randomQuote

/listQuoteIDs

/quote/{quote_id}

/author/{author_id}

/image/{author_id}
