from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-map',
	version=version,
	description="",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Ben Scott',
	author_email='',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.map'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
            map = ckanext.map.plugin:MapPlugin
        [paste.paster_command]
            ckanextmap=ckanext.map.commands.add_geom:AddGeomCommand
	""",
)
