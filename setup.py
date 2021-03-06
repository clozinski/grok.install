from setuptools import setup, find_packages
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.md')
    + '\n' +
    read('CHANGES.md')
    + '\n' +
    'Download\n'
    '********\n'
    )

tests_require = [
    'zope.app.wsgi',
    'zope.configuration',
    'zope.testing',
    ]

setup(
    name='grok',
    version='1.14.2.dev0',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://cheeseshop.python.org/pypi/grok/',
    description='Grok: Now even cavemen can use Zope 3!',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Framework :: Zope3',
        ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'grok >=1.14.1',
        'myapp',
        ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
