from setuptools import setup

setup(
    name='studyspace',
    version='0.1.0',
    packages=['studyspace'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'requests',
    ],
    python_requires='>=3.8',
)
