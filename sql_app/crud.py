from sqlalchemy.orm import Session

from .models import GameModel, HistoryModel
from .schemas import GameCreateSchema, HistorySchema


def create_game(db: Session, game: GameCreateSchema):
    db_game = GameModel(board=game.board, finished=game.finished)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game(db: Session, game_id: int):
    return db.query(GameModel).filter(GameModel.id == game_id).first()


def make_move(db: Session, db_game: Session, history: HistorySchema):
    db_game.board[history.position] = 0 if history.type == "X" else 1
    db_history = HistoryModel(**history.dict(), game_id=db_game.id)
    db.add(db_history)
    db.commit()
    db.refresh(db_game)
