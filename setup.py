from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

with open("README.md", "r") as f:
    long_description = f.read()

exec(compile(open('flask_request_logger/__about__.py').read(), 'flask_request_logger/__about__.py', 'exec'))

setup(
    name='flask-request-logger',
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BbsonLin/flask-request-logger',
    license='MIT',
    author=__author__,
    author_email=__email__,
    packages=['flask_request_logger'],
    install_requires=install_requires,
    zip_safe=False,
    keywords='flask logger',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
)
