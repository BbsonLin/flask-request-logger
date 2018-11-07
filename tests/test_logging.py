from flask_request_logger.models import RequestLog, ResponseLog


def test_logging(app, client):
    @app.route('/test', methods=['GET'])
    def test():
        return 'test response'

    assert client.get('/test').status_code == 200
    # print(RequestLog.query.all())
    assert len(RequestLog.query.all()) != 0
    assert len(ResponseLog.query.all()) != 0
