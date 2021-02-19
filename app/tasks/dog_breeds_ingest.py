import requests

from app.logging import logger
from app.clients.exceptions import HttpServiceException
from app.clients.dogceo import fetch_dog_breeds

from app.database.engine import session_scope
from app.services.dog_service import create_dog_breed


def handler(event, context):
    dog_breeds = None
    try:
        dog_breeds = fetch_dog_breeds()
    except HttpServiceException as _err:
        logger.error(str(_err))
    else:
        ingested_count = 0
        with session_scope() as session:
            for breed, sub_breeds in dog_breeds.items():
                # Create Breed
                breed_params = dict(name=breed)
                created_breed = create_dog_breed(session=session,
                                                 params=breed_params)
                ingested_count += 1
                # Create Sub-breed
                for sub_breed in sub_breeds:
                    ingested_count += 1
                    sub_breed_params = dict(name=sub_breed,
                                            parent_id=created_breed.id)
                    created_sub_breed = create_dog_breed(
                        session=session, params=sub_breed_params)

    return {'ingested_records': ingested_count}