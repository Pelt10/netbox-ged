from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='netbox_ged',
    version='0.2.0',
    description='Manage documents in Netbox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pelt10',
    author_email='contact@lethiec.me',
    url='https://github.com/pelt10/netbox-ged',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords=['netbox', 'netbox-plugin', 'plugin'],
)
