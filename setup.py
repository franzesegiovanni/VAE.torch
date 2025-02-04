#create setup.py file for pip
from setuptools import setup, find_packages

setup(
    name='variational_autoencoders',
    version='0.0.1',
    description='Variational Autoencoder in PyTorch',
    author='AntixK',
    author_email='',
     packages=find_packages(),
    # Add other dependencies here
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
