from fastapi import APIRouter
from fastapi import Depends, Path, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from models.movie import Movie as MovieModel
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movie',tags=['movie'],response_model=List[Movie], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

@movie_router.get('/movie/{id}',tags=['movie'],response_model=Movie, status_code=status.HTTP_200_OK)
def get_movie(id:int = Path(ge=1,le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movies(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='No Encontrado')
    else:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))
    #for item in movies:
    #    if item['id'] == id:
    #        return JSONResponse(status_code=status.HTTP_200_OK, content=item)
    #return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=jsonable_encoder(result))

@movie_router.get('/movies/',tags=['movie'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movie_by_category(category:str = Query(min_length=5,max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='No Encontrado')
    else:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))
    #for item in movies:
    #    if item['category'] == category:
    #        return JSONResponse(status_code=status.HTTP_200_OK, content=item)
    #return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=[])

@movie_router.post('/movies',tags=['movie'], response_model=dict, status_code=status.HTTP_201_CREATED)
def create_movie(movie:Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    #movies.append(movie.dict())
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message':'Se registro la película'})

@movie_router.put('/movie/{id}',tags=['movie'], response_model=dict, status_code=status.HTTP_200_OK)
def update_movie_movies_id(id:int,item:Movie) -> dict:
    
    db = Session()
    result = MovieService(db).get_movies(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content='No de Encontró')
    else:
        MovieService(db).update_movie(id,item)
        return JSONResponse(status_code=status.HTTP_200_OK, content='Se ha modificado')
    
    try:
        index = [movie['id'] for movie in movies].index(id)
        movies[index] = item.dict()
        return JSONResponse(status_code=status.HTTP_200_OK, content={'message':'Se modificado la película'})
    except ValueError:
        return {'error':'Movie not Found'}
    signal = False
    for i in movies:
        if i['id'] == id:
            i['tittle'] = item.tittle
            i['review'] = item.review
            i['year'] = item.year
            i['ranking'] = item.ranking
            i['category'] = item.category
            signal = True
    return signal
    #if signal == False:
    #    raise HTTPException(status_code=404,detail='Movie not found')

@movie_router.delete('/movie/{id}',tags=['movie'], response_model=dict, status_code=status.HTTP_200_OK)
def delete_movie(id:int) -> dict:
    db = Session()
    result = MovieService(db).get_movies(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=[])
    else:
        MovieService(db).delete_movie(id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'message':'Se eliminó la película'})
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(status_code=status.HTTP_200_OK, content={'message':'Se eliminó la película'})
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=[])