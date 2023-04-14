from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI(terms_of_service='https://instagram.com/educhumpitome',description="un intento de api")
app.title = 'Mi aplicación con FastAPI'
app.version = '0.0.1'
app.contact = {
    'name':'Eduardo Chumpitaz',
    'url':'https://instagram.com/educhumpitome',
    'email':'chumpitome@gmail.com'
}
app.license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    }

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        'id':1,
        'tittle':'Avatar',
        'overview':'La mejor pelicula de seres de color azul',
        'year':'2009',
        'ranking':7.8,
        'category':'Acción'
    },
    {
        'id':2,
        'tittle':'Wiñaypacha',
        'overview':'Una pareja de ancianos se quedan a vivir solos en las profundidades de la sierra peruana',
        'year':'2019',
        'ranking':9.5,
        'category':'Documental'
    }
]

@app.get('/',tags=['home'])
def message():
    #return {'msg':'Hola Mundo'}
    return HTMLResponse('<h1>Hola Mundo, soy <b>Eduardo</b></h1>')

