from setuptools import setup
from pathlib import Path

setup(
    name="markdown_mark",
    version="0.0.1",
    license="LGPLv3",
    url="https://github.com/alberic89/markdown_mark",
    description="A markdown python extension that enables you to create <mark> tag by using ==some text== or ???other text???",
    author="alberic89",
    author_email="alberic89@gmx.com",
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    py_modules=['markdown_mark'],
    install_requires=['markdown>=3.0'],
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
