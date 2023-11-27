from setuptools import setup, find_packages

setup(
    name='crfill',
    version='0.0.1',
    description='',
    author='zengxianyu',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
