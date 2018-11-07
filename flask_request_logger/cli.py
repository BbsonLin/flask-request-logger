import os
import sys
import click


def import_application(app_package, req_logger):
    sys.path.append(os.getcwd())
    try:
        _app = __import__(app_package)
    except Exception as e:
        click.secho('Was unable to import {} Error: {}'.format(app_package, e), fg='red')
        exit(3)
    if hasattr(_app, 'req_logger'):
        return getattr(_app, req_logger)
    else:
        click.secho('There in no req_logger var on your package, \
                    you can use req_logger parameter to config', fg='red')
        exit(3)


@click.group('logger')
def logger_cli():
    """
    Flask-Request-Logger commands group
    """
    pass


@logger_cli.command('init_db')
@click.option('--app', default='app', help='Your application init directory (package)')
@click.option('--req_logger', default='req_logger', help='your ReqeustLogger object')
def init_db(app, req_logger):
    from sqlalchemy import create_engine
    from flask_request_logger.database import Base
    from flask_request_logger.models import RequestLog, ResponseLog

    def create_db(db_engine, db_name):
        try:
            db_engine.execute('''CREATE DATABASE IF NOT EXISTS {} charset utf8mb4
                              COLLATE utf8mb4_general_ci'''.format(db_name))
            click.secho('Successfully create db "{}" ...'.format(db_name), fg='green')
        except Exception as e:
            click.secho('Failed to create db, Error: {}'.format(e), fg='red')
            exit(3)

    _req_logger = import_application(app, req_logger)

    click.secho('You\'re using "{}" engine. Your db name is "{}"'.format(
                    _req_logger.db_info.drivername, _req_logger.db_info.database), fg='blue')
    if 'mysql' in _req_logger.db_info.drivername:
        engine = create_engine(
            "{db_info.drivername}://{db_info.username}:{db_info.password}@{db_info.host}/".format(
                db_info=_req_logger.db_info), convert_unicode=True)
        create_db(engine, _req_logger.db_info.database)

    try:
        engine = create_engine(_req_logger.db_info, convert_unicode=True)
        Base.metadata.create_all(bind=engine)
        click.secho('Successfully initialize db ...', fg='green')
    except Exception as e:
        click.secho('Failed to initialize db, Error: {}'.format(e), fg='red')
        exit(3)
