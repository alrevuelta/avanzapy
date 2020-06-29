from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='avanzapy',

    # TODO Single source the version. Currently this has to be changed manually
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.2',
    description='A Python wrapper to interact with Avanza',
    long_description="With this Python wrapper you can interact with the Swedish broker Avanza. You can run two "
                     "types of query: logged in and not logged in. Regarding the first ones you can query your "
                     "balances and open positions, or even send orders to market. If you are not logged with your "
                     "account (maybe you don't have an account or don't want to expose your data) you can still "
                     "use this wrapper to query differentes instruments data (stocks, funds, certificates, etf,...). "
                     "You can get both current price and historical price in different formats",
    url='https://github.com/alrevuelta/avanzapy',
    author='Alvaro Revuelta',
    # author_email='author@example.com',

    classifiers=[
        # How mature is this project?
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='avanza broker trading',
    package_dir={'avanzapy': 'avanzapy'},
    packages=['avanzapy'],
    python_requires='>=3.6',
    install_requires=["aiohttp>=3.6.2",
                      "requests==2.23.0",
                      "pandas==1.0.4",
                      "matplotlib==3.2.1"],

    # package_data={
    #    'sample': ['package_data.dat'],
    # },

    # project_urls={  # Optional
    #    'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #    'Funding': 'https://donate.pypi.org',
    #    'Say Thanks!': 'http://saythanks.io/to/example',
    #    'Source': 'https://github.com/pypa/sampleproject/',
    # },
)
