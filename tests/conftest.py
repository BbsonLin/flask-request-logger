import os
import pytest

TEST_APP_PATH = 'tests/myapp.py'


@pytest.fixture(scope='session')
def app():
    def make_test_app():
        with open(TEST_APP_PATH, 'w') as f:
            for line in [
                'from flask import Flask\n',
                'from flask_request_logger import RequestLogger\n',
                'test_app = Flask(__name__)\n',
                'req_logger = RequestLogger()\n',
                'req_logger.init_app(test_app)\n',
            ]:
                f.write(line)

    make_test_app()

    from myapp import test_app, req_logger
    yield test_app

    if req_logger.db_info.drivername == 'sqlite':
        os.unlink(req_logger.db_info.database)
    if os.path.exists(TEST_APP_PATH):
        os.unlink(TEST_APP_PATH)


@pytest.fixture
def client(app):
    """A test client for the app."""
    app.testing = True
    return app.test_client()
