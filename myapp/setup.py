from setuptools import setup, find_packages

setup(
    name='myapp',
    version='0.1',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='https://github.com/clozinski/grok.install',
    description="""\
Simple Part of the Install package. 
""",
    packages=find_packages('.'),
    package_dir={'': '.'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',

    install_requires=['setuptools',
                      'grok',
                      'grokui.admin',
                      'grokcore.startup',
                      'grokcore.message',
                      ],
    entry_points="""
    [console_scripts]
    interactive_debug_prompt = grokcore.startup.startup:interactive_debug_prompt
    [paste.app_factory]
    main = grokcore.startup:application_factory""",
)
