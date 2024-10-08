from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "prime",
        sources=[
            'prime.pyx',
            "prime.c"
        ]),
]

setup(
    name="prime",
    ext_modules=cythonize(ext_modules),
)
