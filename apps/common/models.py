from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from geoalchemy2 import Geography
from apps.db.database import Base
import enum


class Region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)


class District(Base):
    __tablename__ = "district"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    region_id = Column(UUID(as_uuid=True), ForeignKey("region.id"), nullable=False)
    region = relationship("Region")


class LocationTypeEnum(str, enum.Enum):
    bookshop = "bookshop"
    library = "library"
    home = "home"
    workplace = "workplace"


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, index=True)
    point = Column(Geography(geometry_type='POINT', srid=4326))
    type = Column(Enum(LocationTypeEnum), default=LocationTypeEnum.home)


class Banner(Base):
    __tablename__ = "banner"
    id = Column(Integer, primary_key=True, index=True)
    picture = Column(String, nullable=False)
    title = Column(String(400), nullable=True)
    is_active = Column(Boolean, default=False)


class FAQ(Base):
    __tablename__ = "faq"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(400), nullable=False)
    answer = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)


class PolicyTypeEnum(str, enum.Enum):
    public = "public"
    bookshop = "bookshop"

class PrivacyPolicy(Base):
    __tablename__ = "privacy_policy"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(400), nullable=False)
    description = Column(String, nullable=False)
    type = Column(Enum(PolicyTypeEnum), default=PolicyTypeEnum.public)
    is_active = Column(Boolean, default=False)
