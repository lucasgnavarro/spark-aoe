from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.logging import logger
from app.database.models.base import Base
from app.settings import DATABASE_URL

Engine = create_engine(DATABASE_URL)
session_factory = sessionmaker(bind=Engine)
BoundedSession = scoped_session(session_factory)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = BoundedSession()
    Base.metadata.create_all(Engine)
    logger.debug(f'session_scope retrieve session with {id(session)}')
    try:
        yield session
        BoundedSession.commit()
    except:
        BoundedSession.rollback()
        raise
    finally:
        BoundedSession.remove()
