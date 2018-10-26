from flask import request

from .database import init_db
from .models import RequestLog, ResponseLog


class RequestLogger(object):

    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self._set_default_config(app)

        self.db = init_db(app.config['REQUEST_LOGGER_DB_URI'])

        app.after_request(self._update_database)

    def _set_default_config(self, app):
        app.config.setdefault('REQUEST_LOGGER_DB_URI',
                              'sqlite:///{}/request_log.db'.format(app.root_path))

    def _update_database(self, response):
        req_log = RequestLog(request.method, request.url, request.content_length)
        self.db.add(req_log)
        self.db.commit()
        res_log = ResponseLog(response.status_code, response.content_length, req_log.id)
        self.db.add(res_log)
        self.db.commit()

        return response
