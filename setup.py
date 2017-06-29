"""Package for no_op2 image resizer for reddit"""
from __future__ import unicode_literals
from setuptools import setup, find_packages

import no_op2_resizer

setup(
    name='reddit_no_op2_resizer',
    description='',
    version=no_op2_resizer.__version__,
    license='BSD 3 Clause',
    author='MIT Office of Digital Learning',
    author_email='mitx-devops@mit.edu',
    keywords='reddit',
    packages=find_packages(),
    install_requires=['r2'],
    entry_points={
        # 'r2.plugin':
        #     ['no_op2_resizer = no_op2_resizer:NoOp2Resizer'],
        'r2.provider.image_resizing':
            ['no_op2 = no_op2_resizer.provider:NoOp2ImageResizingProvider'],
    },
    include_package_data=True,
    zip_safe=False,
)
