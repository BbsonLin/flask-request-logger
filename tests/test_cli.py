

def test_init_db(app):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['logger', 'init_db', '--app=myapp'])
    assert 'Successfully' in result.output
