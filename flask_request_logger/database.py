import datetime

from sqlalchemy.ext.declarative import as_declarative

from flask_sqlalchemy import DefaultMeta as SQLModelDefaultMeta


@as_declarative(name='SQLModel', metaclass=SQLModelDefaultMeta)
class SQLModel(object):
    """
    Inspire by flask_builder.models

    Use it and configure it just like flask_sqlalchemy
    """
    __table_args__ = {'extend_existing': True}

    def to_json(self):
        result = dict()
        for key in self.__mapper__.c.keys():
            col = getattr(self, key)
            if isinstance(col, datetime.datetime) or isinstance(col, datetime.date):
                col = col.isoformat()
            result[key] = col
        return result


Base = SQLModel
