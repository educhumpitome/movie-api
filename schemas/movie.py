from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    #tittle: str = Field(default='Mi película',min_length=5,max_length=15)
    tittle: str = Field(min_length=5,max_length=15)
    review: str = Field(min_length=5,max_length=50)
    year: int = Field(le=2022)
    ranking: float = Field(ge=1,le=10)
    category: str = Field(min_length=5,max_length=15)
    
    class Config:
        schema_extra = {
            'example':{
                'id':1,
                'tittle':'Mi película',
                'review':'Descripción de la película',
                'year':2022,
                'ranking':9.8,
                'category':'Categoria de la película'
            }
        }