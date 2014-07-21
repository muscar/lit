from setuptools import setup, find_packages
from codecs import open


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='lit',
    version='0.1',
    author='Alex Muscar',
    author_email='muscar@gmail.com',
    description='Python literate programming',
    long_description=long_description,
    url='https://github.com/muscar/lit',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Pre-processors',
        'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='literate programming markdown html',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['jinja2', 'pygments', 'markdown', 'watchdog', 'termcolor'],
    include_package_data = True,
    entry_points={
        'console_scripts': [
            'lit=lit.lit:main'
        ],
    },
)