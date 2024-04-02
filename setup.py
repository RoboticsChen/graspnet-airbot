from setuptools import setup, find_packages

setup(
    name='graspnet',
    version='0.1',
    description='graspnet',
    author='chenxi-wang',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'tensorboard',
        'numpy',
        'scipy',
        'open3d',
        'Pillow',
        'tqdm',
        'torch',
    ]
)
