from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from booking_hotels.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    First_name = Column(String, nullable=False)
    Last_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    booking = relationship("Bookings", back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"
    

@dataclass
class TokenData():
    username: str
