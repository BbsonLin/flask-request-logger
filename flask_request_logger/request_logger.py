from flask import request
from sqlalchemy.engine.url import make_url

from .cli import logger_cli
from .models import RequestLog, ResponseLog
from .api import RequestLogAPI, ResponseLogAPI, LogAPI


class RequestLogger(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['flask-request-logger'] = self

        self._set_default_config(app)
        self._set_default_cli(app)

        self.db = self._create_db_session(app)
        self.db_info = make_url(app.config['REQUEST_LOGGER_DB_URI'])

        self._set_default_api(app)

        app.after_request(self._logging_req_resp)

    def _set_default_config(self, app):
        app.config.setdefault('REQUEST_LOGGER_DB_NAME', 'request_log')
        app.config.setdefault('REQUEST_LOGGER_DB_URI', 'sqlite:///{}/{}.db'.format(
            app.root_path, app.config['REQUEST_LOGGER_DB_NAME']))

    def _set_default_cli(self, app):
        app.cli.add_command(logger_cli)

    def _set_default_api(self, app):
        req_log_view = RequestLogAPI.as_view('req-log')
        app.add_url_rule('/req-log/', view_func=req_log_view)

        resp_log_view = ResponseLogAPI.as_view('resp-log')
        app.add_url_rule('/resp-log/', view_func=resp_log_view)

        log_view = LogAPI.as_view('logs')
        app.add_url_rule('/logs/', view_func=log_view)

    def _create_db_session(self, app):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import scoped_session, sessionmaker
        from flask_request_logger.database import Base

        engine = create_engine(app.config['REQUEST_LOGGER_DB_URI'], convert_unicode=True)
        db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
        Base.query = db_session.query_property()
        return db_session

    def _logging_req_resp(self, response):
        req_log = RequestLog(request.method, request.url, request.content_length, request.remote_addr, request.user_agent)
        self.db.add(req_log)
        self.db.commit()
        res_log = ResponseLog(response.status_code, response.content_length, req_log.id)
        self.db.add(res_log)
        self.db.commit()

        return response
