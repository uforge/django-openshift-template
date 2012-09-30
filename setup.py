#!/usr/bin/env python

from setuptools import setup

setup(
    name='openshift',
    version='0.2',
    description='OpenShift Generic Django App',
    author='Droidware',
    author_email='info@droidware.it',
    url='http://www.droidware.it',
    dependency_links = ['http://hen.droidware.it/packages/'],
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
