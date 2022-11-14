from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from .database import Base

class GameModel(Base):
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True, index=True)
    board = Column(ARRAY(Integer))
    finished = Column(Boolean, default=True)
    
    histories = relationship("histories", back_populates="game")

class HistoryModel(Base):
    __tablename__ = "histories"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    position = Column(Integer)
    result = Column(Boolean, default=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    
    game = relationship("Game", back_populates="histories")
    