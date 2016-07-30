from setuptools import setup
from dystic import _VERSION

setup(
    name='dystic',
    packages=['dystic'],
    version=_VERSION,
    description='a static site generator using dynamic principles',
    long_description='Please visit https://github.com/MiteshNinja/dystic for more details.',
    author='Mitesh Shah',
    author_email='mitesh@miteshshah.com',
    url='https://github.com/MiteshNinja/dystic',
    download_url='https://github.com/MiteshNinja/dystic/tarball/' + _VERSION,
    keywords=['blog', 'generator', 'static', 'dynamic', 'dystic'],
    classifiers=[],
    install_requires=[
        'mistune', 'jinja2', 'pyyaml', 'pygments'
    ],
    entry_points={
        'console_scripts': [
            'dystic=dystic:main',
        ],
    })
