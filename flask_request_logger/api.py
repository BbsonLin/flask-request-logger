import logging

from flask import jsonify
from flask.views import MethodView
from flask_request_logger.models import RequestLog, ResponseLog

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler())


class RequestLogAPI(MethodView):
    """
    Extend from :class:`flask.views.MethodView`

    An API that mulipulate `request_log` table content.
    """

    def get(self):
        req_logs = [req_log.to_json() for req_log in RequestLog.query.all()]
        LOG.debug('RequestLog.query: {}'.format(req_logs))
        return jsonify(data=req_logs)


class ResponseLogAPI(MethodView):
    """
    Extend from :class:`flask.views.MethodView`

    An API that mulipulate `response` table content.
    """

    def get(self):
        resp_logs = [resp_log.to_json() for resp_log in ResponseLog.query.all()]
        LOG.debug('ResponseLog.query: {}'.format(resp_logs))
        return jsonify(data=resp_logs)
