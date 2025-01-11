from setuptools import setup, find_packages

setup(
    name="fmp_core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author="Jakub Bartnik",
    author_email="jakub@bartnyk.pl",
    description="Core package for stock predictor",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/bartnyk/stock_predictor_core",
    python_requires='>=3.12',
)