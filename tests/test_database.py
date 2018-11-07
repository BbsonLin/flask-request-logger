import os

from utils import get_request_logger


def test_db_exist(app):
    request_logger = get_request_logger(app)
    if request_logger.db_info.drivername == 'sqlite':
        assert os.path.exists(request_logger.db_info.database)
