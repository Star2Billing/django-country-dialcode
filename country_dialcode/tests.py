#
# Django-Country-Dialcode License
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.contrib.auth.models import User
from django.test import TestCase
from common.utils import BaseAuthenticatedClient
from country_dialcode.models import Country, Prefix


class CountryDialcodeAdminView(BaseAuthenticatedClient):
    """Test cases for CountryDialcode Admin Interface."""

    def test_admin_country_view_list(self):
        """Test Function to check admin country list"""
        response = self.client.get("/admin/country_dialcode/country/")
        self.assertEqual(response.status_code, 200)

    def test_admin_country_view_add(self):
        """Test Function to check admin country add"""
        response = self.client.get("/admin/country_dialcode/country/add/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/admin/country_dialcode/country/add/',
            data={'countrycode': 'ESP',
                  'iso2': 'ES',
                  'countryprefix': '34',
                  'countryname': 'Spain',
                  })
        self.assertEqual(response.status_code, 200)


    def test_admin_prefix_view_list(self):
        """Test Function to check admin prefix list"""
        response = self.client.get("/admin/country_dialcode/prefix/")
        self.assertEqual(response.status_code, 200)

    def test_admin_prefix_view_add(self):
        """Test Function to check admin prefix add"""
        response = self.client.get("/admin/country_dialcode/prefix/add/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/admin/country_dialcode/prefix/add/',
            data={'prefix': '34',
                  'destination': 'Spain',
                  'country_id': 198,
                  'carrier_name': 'xyz',
                  'prefix_type': 1})
        self.assertEqual(response.status_code, 200)


class CountryDialcodeModel(TestCase):
    """Test Country, Prefix models"""

    def setUp(self):
        # Country model
        self.country = Country(
            countrycode="ESP",
            iso2='ES',
            countryprefix='34',
            countryname='Spain',
        )
        self.country.save()

        # Prefix model
        self.prefix = Prefix(
            prefix=34,
            destination='Spain',
            country_id=198,
            carrier_name='xyz',
            prefix_type=1
        )
        self.prefix.save()

    def test_country_prefix_name(self):
        self.assertEqual(self.country.countryname, "Spain")
        self.assertEqual(self.prefix.country_name, "Spain")

    def teardown(self):
        self.country.delete()
        self.prefix.delete()


