from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    
    def __init__(self, db) -> None:
        self.db = db
        
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movies(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self, id:int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.tittle = data.tittle
        movie.category = data.category
        movie.ranking = data.ranking
        movie.year = data.year
        movie.review = data.review
        self.db.commit()
        return
    
    def delete_movie(self, id:int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return