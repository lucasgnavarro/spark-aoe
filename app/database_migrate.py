from os.path import join, realpath

from alembic import command
from alembic.config import Config
from app.database.engine import Engine as engine
from app.settings import PROJECT_ROOT


def handler(event, context):
    body = event.get('body', {})
    alembic_ini_path = realpath(
        join(PROJECT_ROOT, 'app', 'database', 'alembic.ini'))

    command_name = body.get('command', 'upgrade')
    revision = body.get('revision', 'head')

    # try:
    alembic_cfg = Config(alembic_ini_path)
    with engine.begin() as connection:
        alembic_cfg.attributes['connection'] = connection
        if command_name == 'upgrade':
            command.upgrade(alembic_cfg, revision)
        else:
            command.downgrade(alembic_cfg, revision)
    return {
        'status': 'success',
        'message': f'alembic {command_name} to revision ({revision})'
    }
    # except Exception as e:

    # return {'status': 'error', 'message': str(e)}
