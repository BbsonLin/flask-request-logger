import sys
import click

from subprocess import Popen, CalledProcessError


def build():
    cmd = [sys.executable, 'setup.py', 'sdist', 'bdist_wheel']
    Popen(cmd).wait()


def push_to_pypi(testing=False):
    try:
        if testing:
            cmd = ['twine', 'upload', '--repository-url', 'https://test.pypi.org/legacy/', 'dist/*']
        else:
            cmd = ['twine', 'upload', 'dist/*']
        process = Popen(cmd)
        output = process.communicate()[0]
        if process.returncode != 0:
            raise CalledProcessError(process.returncode, cmd, output=output)
        else:
            click.secho('Success on pushing build to to (Test)PyPI server ...', fg='green')
    except Exception as e:
        click.secho('Failed to push to (Test)PyPI server, Error: {}'.format(e), fg='red')
        exit(3)


def main():
    if click.confirm('Making build?'):
        build()
        if click.confirm('Push to TestPyPI?'):
            push_to_pypi(testing=True)
            click.secho('Please check out https://test.pypi.org/legacy/ for test result', fg='blue')
        if click.confirm('Continue to push to PyPI?'):
            push_to_pypi()
            click.secho('Please check out https://pypi.org/ for result', fg='blue')


if __name__ == '__main__':
    main()
