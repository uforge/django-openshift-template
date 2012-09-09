#!/usr/bin/env python

from setuptools import setup

setup(
    name='openshift',
    version='1.0',
    description='OpenShift Generic Django App',
    author='Droidware',
    author_email='info@droidware.it',
    url='http://www.droidware.it',
    dependency_links = ['http://hen.droidware.it/packages/'],
    install_requires=['Django', 'PIL', 'droid-common-js', 'droid-django-dajaxice'],
)
