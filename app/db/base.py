from typing import Any
from sqlalchemy import Boolean, Column,DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    created_at = Column(DateTime(timezone=True), default=func.utc_timestamp())
    updated_at = Column(DateTime(timezone=True), onupdate=func.utc_timestamp())
    is_deleted = Column(Boolean, default=False)
    
    __table_args__ = {'mysql_engine':'InnoDB'}
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    def to_schema(self, schema_cls):
        return schema_cls(**self.__dict__)
    
    @classmethod
    def from_schema(cls, schema_obj):
        return cls(**schema_obj.__dict__)