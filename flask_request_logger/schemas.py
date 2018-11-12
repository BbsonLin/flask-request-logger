from marshmallow import fields, Schema
from marshmallow_sqlalchemy import ModelSchema

from flask_request_logger.models import RequestLog, ResponseLog


class RequestLogSchema(ModelSchema):
    class Meta:
        model = RequestLog
        exclude = ('response_log', )


class ResponseLogSchema(ModelSchema):
    class Meta:
        model = ResponseLog
        exclude = ('request', )


class LogSchema(Schema):
    request = fields.Nested(RequestLogSchema)
    response = fields.Nested(ResponseLogSchema)
