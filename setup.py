from pathlib import Path

import setuptools

from dlestxetx import __version__

README = Path(__file__).parent / 'README.rst'

setuptools.setup(
    name='dlestxetx',
    version=__version__,
    description='DLE/STX/ETX packet encoder/decoder',
    long_description=README.read_text(),
    url='https://github.com/Lx/python-dlestxetx',
    author='Alex Peters',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
        'Typing :: Typed',
    ],
    keywords='DLE STX ETX',
    py_modules=['dlestxetx'],
    python_requires='>=3.6, <4',
)
