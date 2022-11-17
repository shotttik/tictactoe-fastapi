from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList
from .database import Base


class GameModel(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    board = Column(MutableList.as_mutable(ARRAY(Integer)))
    finished = Column(Boolean, default=False)
    winner = Column(Integer, default=None)
    last_move = Column(Integer, default=None)

    histories = relationship("HistoryModel", back_populates="game")


class HistoryModel(Base):
    __tablename__ = "histories"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer)
    position = Column(Integer)
    game_id = Column(Integer, ForeignKey("games.id"))

    game = relationship("GameModel", back_populates="histories")
