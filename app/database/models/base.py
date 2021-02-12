from typing import Type, Union, Optional

import logging
import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import and_

from marshmallow_sqlalchemy.schema import ModelSchemaMeta

from app.database.exceptions import ObjectDoesNotExist

logger = logging.getLogger()

Base = declarative_base()
