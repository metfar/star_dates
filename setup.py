from setuptools import setup, find_packages;

setup(
    name='star_dates',
    version='1.0.1',
    description='Conversor de fechas a Stardate con precisión horaria desde el año 2000',
    author='William Martinez Bas',
    author_email='metfar@gmail.com',
    license='MIT',
    packages=find_packages(),
    py_modules=['star_dates_module'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'stardate=star_dates_module:main',
        ],
    },
);
