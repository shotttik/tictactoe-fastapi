from pydantic import BaseModel
from typing import List

class HistoryBaseSchema(BaseModel):
    type: str
    position: int
    result: bool
    

class HistoryCreateSchema(HistoryBaseSchema):
    pass

class HistorySchema(HistoryBaseSchema):
    id: int
    game_id: int
    
    class Config:
        orm_mode = True

class GameBaseSchema(BaseModel):
    board: List = [
        "","","",
        "","","",
        "","","",
        ]
    finished: bool = False

class GameCreateSchema(GameBaseSchema):
    pass


class GameSchema(GameBaseSchema):
    id: int
    histories: List[HistorySchema] = []
    
    class Config:
        orm_mode = True
