from fastapi import FastAPI, HTTPException, Depends
from sql_app.models import Base
from sql_app.schemas import GameSchema, GameCreateSchema, HistorySchema, HistoryCreateSchema
from sql_app.database import SessionLocal, engine
from sql_app.crud import create_game, get_game, make_move
from sql_app.utils import error_message

from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/start")
def start(game: GameCreateSchema, db: Session = Depends(get_db)):
    create_game(db=db, game=game)
    return {"game_id": 0}


@app.post("/move/{game_id}")
def move(game_id, history: HistoryCreateSchema, db: Session = Depends(get_db)):
    db_game = get_game(db=db, game_id=game_id)
    if not db_game:
        return JSONResponse(
            error_message("Game not found"), 404)

    if db_game.finished == True:
        return JSONResponse(
            error_message("Game already finished"), 403)

    htype = history.type.upper()
    if htype != "X" and htype != "Y":
        return JSONResponse(
            error_message("Invalid input of type"), 400)

    hpos = history.position
    if hpos < 0 and hpos > 8:
        return JSONResponse(
            error_message("Invalid input of position, must be between 0 and 8"), 400)

    if db_game.board[history.position] is not None:
        return JSONResponse(
            error_message("invalid_position"), 400)

    make_move(db=db, db_game=db_game, history=history)

    return JSONResponse({"result": "success"}, 200)


@app.get("/check/{game_id}")
def check(game_id):
    return {"game": "finished", "winner": None}
