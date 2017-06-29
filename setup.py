from setuptools import setup, find_packages

setup(
    name='helloworld',
    version='0.1',
    author='GYCHEN',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
