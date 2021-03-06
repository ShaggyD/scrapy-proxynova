from setuptools import setup

setup(
    name='scrapy-proxynova',
    version='0.1.0',
    description='Allows scrapy to use proxy list from proxynova.com',
    keywords='scrapy proxy',
    license='New BSD License',
    author="Alexander Artemenko, Francois Dang Ngoc",
    author_email='svetlyak.40wt@gmail.com, francois.dangngoc@gmail.com',
    url='http://github.com/darthbear/scrapy-proxynova/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    packages=[
        'scrapy_proxynova',
    ],
    install_requires=[
        'requests'
    ],
)
