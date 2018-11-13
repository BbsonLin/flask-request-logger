import logging

from flask import jsonify
from flask.views import MethodView
from flask_request_logger.utils import get_logs, get_request_logs, get_response_logs

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(logging.StreamHandler())


class RequestLogAPI(MethodView):
    """
     | Extend from :class:`flask.views.MethodView`
     | An API that mulipulate `request_log` table content.
     | This API default added rules on endpoints **/req-log/**
    """

    def get(self):
        req_logs = get_request_logs()
        LOG.debug('RequestLog.query: {}'.format(req_logs))
        return jsonify(data=req_logs)


class ResponseLogAPI(MethodView):
    """
     | Extend from :class:`flask.views.MethodView`
     | An API that mulipulate `response_log` table content.
     | This API default added rules on endpoints **/resp-log/**
    """

    def get(self):
        resp_logs = get_response_logs()
        LOG.debug('ResponseLog.query: {}'.format(resp_logs))
        return jsonify(data=resp_logs)


class LogAPI(MethodView):
    """
     | Extend from :class:`flask.views.MethodView`
     | An API that combine `request_log` and `response_log` by using marshmallow schema.
     | This API default added rules on endpoints **/logs/**
    """

    def get(self):
        from flask_request_logger.schemas import LogSchema

        logs = get_logs()
        LOG.debug('Logs: {}'.format(logs))
        log_schema = LogSchema(many=True)
        return jsonify(data=log_schema.dump(logs).data)
