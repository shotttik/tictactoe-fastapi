from fastapi import FastAPI
from sql_app.models import Base
from sql_app.schemas import GameSchema, GameCreateSchema
from sql_app.database import SessionLocal, engine
from sql_app.crud import create_game

from sqlalchemy.orm import Session
from fastapi import Depends


Base.metadata.create_all(bind=engine)

app = FastAPI()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/start", response_model=GameSchema)
async def start(game: GameCreateSchema, db: Session = Depends(get_db)):
    db_game = create_game(db=db, game=game)
    return {"game_id": 0}


@app.get("/move/{game_id}")
async def move(game_id):
    return {"result": "success"}


@app.get("/check/{game_id}")
async def check(game_id):
    return {"game": "finished", "winner": None}