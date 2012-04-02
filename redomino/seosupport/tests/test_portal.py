# Copyright (c) 2010 Redomino srl (http://redomino.com)
# Authors: Davide Moro <davide.moro@redomino.com> and contributors (see docs/CONTRIBUTORS.txt)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.

from redomino.seosupport.tests.base import TestCase


class TestPortal(TestCase):
    """ """

    def test_dependencies(self):
        """ Dependencies installed? """
        self.assertTrue(self.portal.portal_quickinstaller.isProductInstalled('googlesitemap.common'))

    def test_sitemap(self):
        """Test sitemap.xml.gz == True"""
        self.assertTrue(self.portal.portal_properties['site_properties'].enable_sitemap)

    def test_skins(self):
        """Test if the skin layer is installed"""
        self.assertTrue('redomino_seosupport' in self.portal.portal_skins)

    def test_robots_txt(self):
        """Test if robots.txt is in the skin layer"""
        skin = self.portal.portal_skins['redomino_seosupport']
        self.assertTrue('robots.txt' in skin)

    def test_javascript(self):
        """ Test javascript registration """
        portal_javascripts = self.portal.portal_javascripts
        self.assertTrue('redomino_seo.js' in portal_javascripts.getResourceIds())

 


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestPortal))
    return suite


