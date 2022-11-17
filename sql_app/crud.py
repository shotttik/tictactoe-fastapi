from sqlalchemy.orm import Session

from .models import GameModel, HistoryModel
from .schemas import GameCreateSchema, HistorySchema
from .utils import check_game_finished


def create_game(db: Session, game: GameCreateSchema) -> int:
    db_game = GameModel(board=game.board)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game.id


def get_game(db: Session, game_id: int):
    return db.query(GameModel).filter(GameModel.id == game_id).first()


def make_move(db: Session, db_game: Session, history: HistorySchema):
    history.type = 0 if history.type == "X" else 1
    db_game.board[history.position] = history.type
    db_game.last_move = history.type

    if check_game_finished(db_game.board):
        db_game.finished = True
        db_game.winner = history.type

    db_history = HistoryModel(**history.dict(), game_id=db_game.id)
    db.add(db_history)
    db.commit()
    db.refresh(db_game)


def get_history(db: Session):
    games_db = db.query(GameModel).order_by("id").all()
    return [game.serialize for game in games_db]
