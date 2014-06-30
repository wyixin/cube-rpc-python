from setuptools import setup, find_packages

setup(
    name = 'cubi',
    version = '0.0.3',
    keywords = ('cube', 'cubi', 'cube-rpc'),
    description = 'python implementation for Cube RPC protocol',
    license = 'MIT License',
    install_requires = ['bp>=0.0.3'],

    author = 'http://www.liaohuqiu.net',
    author_email = 'liaohuqiu@gmail.com',
    url = 'https://github.com/liaohuqiu/cube-rpc-python',

    packages = find_packages(),
    platforms = 'any',
)