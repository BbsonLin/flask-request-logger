=================
API Documentation
=================

.. toctree::
    :maxdepth: 2

flask_request_logger
====================

.. currentmodule:: flask_request_logger

RequestLogger
-------------

.. module:: flask_request_logger

.. autoclass:: RequestLogger

    .. automethod:: __init__
    .. automethod:: init_app


flask_request_logger.database
=============================

.. module:: flask_request_logger.database

.. autoclass:: SQLModel

    .. automethod:: to_json

.. attribute:: Base


flask_request_logger.models
===========================

.. module:: flask_request_logger.models

.. autoclass:: RequestLog

    .. automethod:: __init__

.. autoclass:: ResponseLog
    
    .. automethod:: __init__


flask_request_logger.api
========================

.. module:: flask_request_logger.api

.. autoclass:: RequestLogAPI

.. autoclass:: ResponseLogAPI