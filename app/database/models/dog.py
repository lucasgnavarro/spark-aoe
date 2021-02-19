from datetime import datetime

from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.database.models import Base, generate_uuid


class DogBreed(Base):
    __tablename__ = 'dog_breeds'

    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    name = Column(String)
    parent_id = Column(UUID(as_uuid=True),
                       ForeignKey('dog_breeds.id'),
                       nullable=True,
                       default=None)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
