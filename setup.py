from setuptools import setup

__version__ = '0.1'

setup(
      name='overapi',
      version=__version__,

      packages=['overwatch_api'],

      description='Overwatch API Wrapper',
      url='',
      author='Marco Visconti',
      license='MIT',
      install_requires=['requests']
)