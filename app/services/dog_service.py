from sqlalchemy.orm.session import Session

from app.database.models.dog import DogBreed


def create_dog_breed(session: Session, params: dict) -> DogBreed:
    dog_breed = DogBreed(**params)
    session.add(dog_breed)
    session.flush()
    return dog_breed
