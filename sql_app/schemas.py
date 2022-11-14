from pydantic import BaseModel
from typing import List

class HistoryBase(BaseModel):
    type: str
    position: int
    result: bool
    

class HistoryCreate(HistoryBase):
    pass

class History(HistoryBase):
    id: int
    game_id: int
    
    class Config:
        orm_mode = True

class GameBase(BaseModel):
    board: List[int] = []
    finished: bool

class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    histories: List[History] = []
    
    class Config:
        orm_mode = True
