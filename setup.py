from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pytheons.pyunit',
    version='1.0.3',
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
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'docopt',
        'PyYAML'
    ]

)
