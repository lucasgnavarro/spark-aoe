from typing import Type, Union, Optional

import logging
import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import and_

logger = logging.getLogger()

Base = declarative_base()

def generate_uuid():
    return uuid.uuid4()