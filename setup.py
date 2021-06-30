from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme_description = f.read()

setup(
    name ="googlesearch",
    packages = ["googlesearch"],
    version = "1.0.0",
    license = "MIT License",
    description = "This module lets you use Google Searching capabilities right from your Python code",
    author = "Anime no Sekai",
    author_email = "niichannomail@gmail.com",
    url = "https://github.com/Animenosekai/googlesearch",
    download_url = "https://github.com/Animenosekai/googlesearch/archive/v1.0.0.tar.gz",
    keywords = ['python', 'Anime no Sekai', "animenosekai", "googlesearch"],
    install_requires = ['beautifulsoup4', 'requests', 'pyuseragents', 'inquirer'],
    classifiers = ['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.2', 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9'],
    long_description = readme_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    python_requires='>=3.2, <4',
    entry_points={
        'console_scripts': [
            'googlesearch = googlesearch.__main__:main'
        ]
    },
    package_data={
        'googlesearch': ['LICENSE'],
    },
)