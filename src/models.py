from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    planets: Mapped[List["FavoritePlanet"]] = relationship()
    characters: Mapped[List["FavoritePeople"]] = relationship()


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model): 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(40), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    species: Mapped[str] = mapped_column(String(40), nullable=False)
    character: Mapped[List["FavoritePeople"]] = relationship(back_populates="People")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "species": self.species,
            "charachter": self.character
        }
    
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    rotation_period: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    gravity: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    terrain: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)


class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_people: Mapped[int] = mapped_column(ForeignKey("people.id"), nullable=True)
    user_id: Mapped