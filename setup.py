#!/usr/bin/env python

from setuptools import setup

setup(
    name='openshift',
    version='0.2',
    description='OpenShift Generic Django App',
    author='uforge',
    author_email='info@uforge.it',
    url='http://www.uforge.it',
    dependency_links = ['http://hen.uforge.it/packages/'],
    install_requires=['Django',
                      'PIL',
                      'eco',
                      'django-pipeline',
                      'django-pipeline-compass',
                      'django-pipeline-eco',
                      'droid-common-js',
                      'droid-django-dajaxice',
                      'south',
                      'django-debug-toolbar',
                      ],
)
