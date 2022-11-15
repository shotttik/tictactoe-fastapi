from sqlalchemy.orm import Session

from .models import GameModel, HistoryModel
from .schemas import GameCreateSchema, HistoryCreateSchema, HistorySchema

def create_game(db: Session, game: GameCreateSchema):
    db_game = GameModel(board=game.board, finished=game.finished)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game(db: Session, game_id: int):
    return db.query(GameModel).filter(GameModel.id == game_id).first()


def create_user_item(db: Session, item: HistoryCreateSchema, game_id: int):
    db_item = HistoryModel(**item.dict(), game_id=game_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item