from fastapi import FastAPI, HTTPException, Depends
from sql_app.models import Base
from sql_app.schemas import GameSchema, GameCreateSchema, HistorySchema, HistoryCreateSchema
from sql_app.database import SessionLocal, engine
from sql_app.crud import create_game, get_game

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
@app.post("/start", response_model=GameSchema) 
ERROR -> field required (type=value_error.missing)
'''
@app.post("/start")
def start(game: GameCreateSchema, db: Session = Depends(get_db)):
    create_game(db=db, game=game)    
    return {"game_id": 0}


@app.post("/move/{game_id}")
def move(game_id, history: HistoryCreateSchema,db: Session = Depends(get_db)):
    db_game = get_game(db=db, game_id=game_id)
    if not db_game:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_game.board[history.position] = history.type
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    
    return {"result": "success"}


@app.get("/check/{game_id}")
def check(game_id):
    return {"game": "finished", "winner": None}