#!/usr/bin/env python

from setuptools import Extension, setup

if __name__ == "__main__":
    setup(
	    ext_modules	= [Extension("spidev", ["spidev_module.c"])]
    )
