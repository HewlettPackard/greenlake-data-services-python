"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "greenlake_data_services"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="HPE Data Services Cloud Console API",
    author="OpenAPI Generator community",
    author_email="sijeesh.kattumunda@hpe.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "HPE Data Services Cloud Console API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    HPE Data Services Cloud Console API  # noqa: E501
    """
)
