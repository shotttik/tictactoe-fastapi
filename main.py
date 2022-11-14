from fastapi import FastAPI

app = FastAPI()


@app.get("/start")
async def start():
    return {"game_id": 0}


@app.get("/move/{game_id}")
async def move(game_id):
    return {"result": "success"}


@app.get("/check/{game_id}")
async def check(game_id):
    return {"game": "finished", "winner": None}