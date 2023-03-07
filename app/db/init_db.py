from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

# make sure all SQL Alchemy models are imported before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
    
    
