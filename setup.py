from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="adaptiveflow",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    description="adaptiveflow",
    author="Active Flow",
    author_email="adaptiveflow@mails.xxx.edu.cn",
)