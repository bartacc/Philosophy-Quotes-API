from fastapi import FastAPI

app = FastAPI()


@app.get('/randomQuote')
def get_random_quote():
    return({'Random quote': 'description'})

@app.get('/quote/{quoteID}')
def get_quote(quoteID: int):
    return({'Quote': quoteID})

@app.get('/author/{authorID}')
def get_author(authorID: int):
    return({'Author': authorID})

@app.get('/image/{authorID}')
def get_image(authorID: int):
    return({'Image': authorID})