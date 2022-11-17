from fastapi import FastAPI, HTTPException, Depends
from sql_app.models import Base
from sql_app.schemas import GameCreateSchema, HistorySchema, HistoryCreateSchema
from sql_app.database import SessionLocal, engine
from sql_app.crud import create_game, get_game, make_move, get_history
from sql_app.utils import error_message, draw_board

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
async def start(game: GameCreateSchema, db: Session = Depends(get_db)):
    game_id = create_game(db=db, game=game)
    return {"game_id": game_id}


@app.post("/move/{game_id}")
async def move(game_id, history: HistoryCreateSchema, db: Session = Depends(get_db)):
    db_game = get_game(db=db, game_id=game_id)
    if not db_game:
        return JSONResponse(
            error_message("Game not found."), 404)

    if db_game.finished == True:
        return JSONResponse(
            error_message("Game already finished."), 403)

    htype = history.type.upper()
    if htype != "X" and htype != "Y":
        return JSONResponse(
            error_message("Invalid input of type."), 400)

    if db_game.last_move == 0 and htype == "X":
        return JSONResponse(
            error_message(f"Its not X move."), 403)

    if db_game.last_move == 1 and htype == "Y":
        return JSONResponse(
            error_message(f"Its not Y move."), 403)

    hpos = history.position
    if hpos < 0 and hpos > 8:
        return JSONResponse(
            error_message("Invalid input of position, must be between 0 and 8."), 400)

    if db_game.board[history.position] is not None:
        return JSONResponse(
            error_message("invalid_position."), 400)

    make_move(db=db, db_game=db_game, history=history)

    return JSONResponse({"result": "success"}, 200)


@app.post("/check/{game_id}")
async def check(game_id, db: Session = Depends(get_db)):
    db_game = get_game(db=db, game_id=game_id)
    if not db_game:
        return JSONResponse(
            error_message("Game not found"), 404)

    board = draw_board(db_game.board)

    if db_game.finished == True:
        return JSONResponse(
            {"game": "finished", "winner": db_game.winner}, 200)

    # return {"game": "in_progress", "board": board}
    return {"game": "in_progress"}


@app.post("/history")
async def history(db: Session = Depends(get_db)):
    history = get_history(db=db)
    return JSONResponse({'data': history}, 200)
