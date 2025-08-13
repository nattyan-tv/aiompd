from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    README = f.read()


setup(
    name="aiompd",
    version="0.4.0",
    description="MPD (Music Player Daemon) client for asyncio",
    long_description=README,
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: System :: Networking",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
    ],
    # author='Alexander Zelenyak', # Original author
    # author_email='zzz.sochi@gmail.com', # Original author email
    url="https://github.com/zzzsochi/aiompd",
    keywords=["mpd", "asyncio"],
    packages=find_packages(),
)
