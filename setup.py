from setuptools import setup, find_packages

setup(
    name='newproject',
    version='0.0',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    package_data={
        'newproject': ['data/*'],
    },
    license='MIT',
    description='newproject template for the Center for Renal Precision Medicine at the University of Texas Health San Antonio.',
    long_description=open('README.md').read(),
    #install_requires=[''],
    url='https://github.com/dmontemayor/newproject',
    author='Daniel Montemayor',
    author_email='montemayord2@uthscsa.edu',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
)
