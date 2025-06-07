from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
import enum
import datetime

Base = declarative_base()


class CoverTypeEnum(str, enum.Enum):
    hard = "hard"
    soft = "soft"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    picture = Column(String)
    name = Column(String(100))
    description = Column(Text, nullable=True)
    author = Column(String(150))
    cover_type = Column(Enum(CoverTypeEnum))
    price = Column(Integer)
    pages = Column(Integer)
    publication_year = Column(Integer)
    isbn = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    is_banned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="books")
    views = relationship("BookView", back_populates="book")
    likes = relationship("BookLike", back_populates="book")
    comments = relationship("BookComment", back_populates="book")


class BookView(Base):
    __tablename__ = "book_views"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="book_views")
    book = relationship("Book", back_populates="views")


class BookLike(Base):
    __tablename__ = "book_likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="book_likes")
    book = relationship("Book", back_populates="likes")


class BookComment(Base):
    __tablename__ = "book_comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    comment = Column(Text)
    parent_id = Column(Integer, ForeignKey("book_comments.id"), nullable=True)
    is_banned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User")
    book = relationship("Book", back_populates="comments")
    replies = relationship("BookComment", backref="parent", remote_side=[id])
    likes = relationship("BookCommentLike", back_populates="comment")


class BookCommentLike(Base):
    __tablename__ = "book_comment_likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    comment_id = Column(Integer, ForeignKey("book_comments.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User")
    comment = relationship("BookComment", back_populates="likes")
