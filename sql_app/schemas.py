from pydantic import BaseModel
from typing import List, Union


class HistoryBaseSchema(BaseModel):
    type: str
    position: int


class HistoryCreateSchema(HistoryBaseSchema):
    pass


class HistorySchema(HistoryBaseSchema):
    id: int
    game_id: int

    class Config:
        orm_mode = True


class GameBaseSchema(BaseModel):
    board: List = [
        None, None, None,
        None, None, None,
        None, None, None,
    ]


class GameCreateSchema(GameBaseSchema):
    pass


class GameSchema(GameBaseSchema):
    id: int
    finished: bool = False
    winner: Union[int, None] = None
    last_move: Union[int, None] = None
    histories: List[HistorySchema] = []

    class Config:
        orm_mode = True
