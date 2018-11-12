from flask import current_app
from flask_request_logger.models import RequestLog, ResponseLog


def _get_request_logger():
    try:
        return current_app.extensions['flask-request-logger']
    except KeyError:
        raise RuntimeError("You must initialize a RequestLogger with this flask "
                           "application before using this method")


def get_request_logs():
    return [req_log.to_json() for req_log in RequestLog.query.all()]


def get_response_logs():
    return [resp_log.to_json() for resp_log in ResponseLog.query.all()]


def get_logs():
    logs_list = list()
    logs = ResponseLog.query.join(RequestLog, ResponseLog.request_id == RequestLog.id).all()
    for log in logs:
        logs_list.append(dict(request=log.request, response=log))

    return logs_list
