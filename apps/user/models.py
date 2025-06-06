from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from database import Base
import enum


class UserRoles(str, enum.Enum):
    SUPERADMIN = 'superadmin'
    ADMIN = 'admin'
    SIMPLE = 'simple'
    BOOKSHOP = 'bookshop'
    LIBRARY = 'library'


class Languages(str, enum.Enum):
    UZBEK = 'uzbek'
    ENGLISH = 'english'
    RUSSIAN = 'russian'


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    bio = Column(String(255), nullable=True)

    phone_number = Column(String(15), unique=True, nullable=True)
    phone_is_visible = Column(Boolean, default=False)
    location_is_visible = Column(Boolean, default=False)

    telegram_id = Column(String(77), unique=True, nullable=False, index=True)
    language = Column(SqlEnum(Languages), default=Languages.UZBEK)
    role = Column(SqlEnum(UserRoles), default=UserRoles.SIMPLE)
    is_active = Column(Boolean, default=True)
    picture = Column(String, default='users/pictures/default_user.png')

    district_id = Column(Integer, ForeignKey('districts.id'), nullable=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=True)

    district = relationship("District", back_populates="users")
    location = relationship("Location", back_populates="users")

    otp = relationship("Otp", back_populates="user", uselist=False)



class Otp(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, index=True)
    otp_code = Column(String(6), nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="otp")
