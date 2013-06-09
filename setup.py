from distutils.core import setup
from beautifulhue.api import __version__

setup(
    name='BeautifulHue',
    version=__version__,
    author='Allan Bunch',
    packages=['beautifulhue', 'beautifulhue.api', 'beautifulhue.lib'],
    url='https://github.com/allanbunch/beautifulhue',
    license='MIT',
    description='A Python module for the Philips Hue Lighting System API.',
    long_description=open('README.txt').read(),
    install_requires=[
        "httplib2 >= 0.8",
    ],
    platforms="Cross Platform",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        ],
)