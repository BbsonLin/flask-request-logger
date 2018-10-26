from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name='flask-request-logger',
    version='0.1.0',
    url='https://github.com/BbsonLin/flask-request-logger',
    license='MIT',
    author='Bobson Lin',
    author_email='bobson801104@gmail.com',
    packages=['flask_request_logger'],
    install_requires=install_requires
)
