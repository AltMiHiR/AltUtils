from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='AltUtils',
    version='1.0.0',
    description='Utility Classes and Functions',
    author='xMiHiR',
    author_email='thexboy131@gmail.com',
    url='https://github.com/AltMiHiR/AltUtils',
    packages=find_packages(),  # Automatically find and include your packages
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
