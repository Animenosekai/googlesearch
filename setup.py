from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme_description = f.read()

setup(
    name ="module_name",
    packages = ["module_name"],
    version = "1.0.0",
    license = "MIT License",
    description = "module_description",
    author = "Anime no Sekai",
    author_email = "niichannomail@gmail.com",
    url = "https://github.com/Animenosekai/module_name",
    download_url = "https://github.com/Animenosekai/module_name/archive/v1.0.0.tar.gz",
    keywords = ['python', 'Anime no Sekai', "animenosekai", "module_name"],
    install_requires = ['typing; python_version<"3.5"'],
    classifiers = ['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.2', 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9'],
    long_description = readme_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    python_requires='>=3.2, <4',
    # if a cli version is available
    # entry_points={
    #       'console_scripts': [
    #           'module_name = module_name.__main__:main'
    #       ]
    # },
    package_data={
        'module_name': ['LICENSE'],
    },
)