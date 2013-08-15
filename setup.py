from setuptools import setup

# From http://bugs.python.org/issue15881
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='mqtt-watchdir',
    version='1.2',
    author='Jan-Piet Mens',
    author_email='jpmens@gmail.com',
    url="https://github.com/jpmens/mqtt-watchdir",
    description='Recursively watch a directory for modifications and publish file content to an MQTT broker',
    license='BSD License',
    scripts=[
        "mqtt-watchdir.py"
    ],
    install_requires=[
        'watchdog',
        'mosquitto',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications',
        'Topic :: Internet',
        ]

)
