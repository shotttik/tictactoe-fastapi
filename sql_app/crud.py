from sqlalchemy.orm import Session

from .models import GameModel
from .schemas import GameCreateSchema

def create_game(db: Session, game: GameCreateSchema):
    db_game = GameModel(board=game.board, finished=game.finished)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
