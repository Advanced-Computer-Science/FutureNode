from setuptools import setup

setup(
    name='FutureNode',
    packages=['futurenode', 'analyze', 'api', 'predict', 'tests'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
