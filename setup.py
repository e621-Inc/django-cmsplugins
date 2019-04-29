from __future__ import unicode_literals

import os
from setuptools import find_packages, setup


version = __import__('cmsplugins').__version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-cmsplugins",
    version=version,
    url='http://github.com/rouxcode/django-cmsplugins',
    license='MIT',
    platforms=['OS Independent'],
    description='Django CMS plugin collection',
    long_description=read('README.rst'),
    author=u'Alaric Maegerle',
    author_email='info@rouxcode.ch',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    install_requires=(
        'cssselect>=0.9.2',
        'Django>=1.11,<2.0',
        'django-cms>=3.4',
        'django-filer>=1.3.0',
        'googlemaps>=2.4.4',
        'lxml>=3.6.4',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
