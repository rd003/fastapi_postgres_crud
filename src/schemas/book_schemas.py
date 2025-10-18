from pydantic import BaseModel, ConfigDict,Field

class BookCreate(BaseModel):
    title:str = Field(min_length=1,max_length=50)
    author:str = Field(min_length=1,max_length=50)

class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) #  allows Pydantic to read data from ORM model attributes directly!
    id:int
    title:str
    author:str
