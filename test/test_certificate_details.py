"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.cert_associated_links import CertAssociatedLinks
from greenlake_data_services.model.certificate_details_enddate import CertificateDetailsEnddate
from greenlake_data_services.model.certificate_details_startdate import CertificateDetailsStartdate
globals()['CertAssociatedLinks'] = CertAssociatedLinks
globals()['CertificateDetailsEnddate'] = CertificateDetailsEnddate
globals()['CertificateDetailsStartdate'] = CertificateDetailsStartdate
from greenlake_data_services.model.certificate_details import CertificateDetails


class TestCertificateDetails(unittest.TestCase):
    """CertificateDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCertificateDetails(self):
        """Test CertificateDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CertificateDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
