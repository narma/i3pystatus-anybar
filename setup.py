#!/usr/bin/env python

from setuptools import setup

setup(name="i3pystatus_anybar",
      version="1.0",
      description="AnyBar widget for i3pystatus",
      url="http://github.com/narma/i3pystatus-anybar",
      license="MIT",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: X11 Applications",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3",
          "Topic :: Desktop Environment :: Window Managers",
      ],
      packages=[
          "i3pystatus_anybar",
      ],
      install_requires=["i3pystatus"],
      zip_safe=True,
      )
