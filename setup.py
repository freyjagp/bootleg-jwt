"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
from setuptools import setup
from decouple import config
import pathlib


here = pathlib.Path(__file__).parent.resolve()


long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="bootleg-jwt",
    version=config('VERSION'),
    description="Sign tokens with blake2b, then verify them.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/freyjagp/bootleg-jwt",
    author="Freyja Odinthrir",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="cryptography, tokens, hashing",
    package_dir={"bootleg_jwt": "src/bootleg_jwt"},
    python_requires=">=3.10, <4",
    install_requires=["pydantic", "python-decouple", "cryptography"],
    project_urls={
        "Bug Reports": "https://github.com/freyjagp/bootleg-jwt/issues",
        # "Funding": "https://donate.pypi.org",
        # "Say Thanks!": "http://saythanks.io/to/example",
        "Source": "https://github.com/freyjagp/bootleg-jwt/",
    },
)
