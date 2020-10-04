from setuptools import setup, find_packages

setup(
    name='pytheons.pyunit',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/pytheons/pyunit',
    license='MIT',
    author='pytheons',
    scripts=['pyunit'],
    author_email='maveilthain@gmail.com',
    include_package_data=True,
    description=' '.join([
        'pyunit is wrapper for PyUnit (uniittest) framework',
        'with one important extension (syntax suger) by `@ test` decorator'
    ]),
    install_requires=[
        'docopt'
    ]

)
