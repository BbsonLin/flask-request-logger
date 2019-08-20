from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from .database import Base


class RequestLog(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)
    method = Column(String(50))
    url = Column(String(255))
    content_length = Column(Integer, nullable=True)
    remote_addr = Column(String(50))
    user_agent = Column(String(255))

    def __init__(self, method, url, content_length, remote_addr, user_agent):
        self.method = method
        self.url = url
        self.content_length = content_length
        self.timestamp = datetime.utcnow()  # Current time normalized as UTC         
        self.remote_addr = remote_addr
        self.user_agent = user_agent.string

    def __repr__(self):
        return ("<{class_name}("
                "id={self.id}, "
                "method='{self.method}', "
                "url='{self.url}', "
                "content_length={self.content_length}, "
                "timestamp={self.timestamp}, "
                "remote_addr='{self.remote_addr}', "
                "user_agent='{self.user_agent}', "
                ")>".format(
                    class_name=self.__class__.__name__,
                    self=self
                ))

class ResponseLog(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    status_code = Column(Integer)
    content_length = Column(Integer, nullable=True)
    request_id = Column(Integer, ForeignKey('request_log.id'))
    request = relationship("RequestLog", backref=backref("response_log", uselist=False))

    def __init__(self, status_code, content_length, request_id):
        self.status_code = status_code
        self.content_length = content_length
        self.request_id = request_id

    def __repr__(self):
        return ("<{class_name}("
                "id={self.id}, "
                "status_code={self.status_code}, "
                "content_length={self.content_length}, "
                "request_id={self.request_id}"
                ")>".format(
                    class_name=self.__class__.__name__,
                    self=self
                ))
