##################################################################################
#    Copyright (c) 2004-2009 Utah State University, All rights reserved.
#    Portions copyright 2009 Massachusetts Institute of Technology, All rights reserved.
#                                                                                 
#    This program is free software; you can redistribute it and/or modify         
#    it under the terms of the GNU General Public License as published by         
#    the Free Software Foundation, version 2.                                      
#                                                                                 
#    This program is distributed in the hope that it will be useful,              
#    but WITHOUT ANY WARRANTY; without even the implied warranty of               
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                
#    GNU General Public License for more details.                                 
#                                                                                 
#    You should have received a copy of the GNU General Public License            
#    along with this program; if not, write to the Free Software                  
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA    
#                                                                                 
##################################################################################

__author__  = '''Brent Lambert, David Ray, Jon Thomas, Shane Graber'''
__version__   = '$ Revision 0.0 $'[11:-2]

from Products.CMFPlone.tests import PloneTestCase
from unittest import TestSuite, makeSuite
from Testing import ZopeTestCase
from Testing.ZopeTestCase import user_name
from AccessControl import Unauthorized
from base import PloneBookmarkletsTestCase
from collective.plonebookmarklets.interfaces import IPloneBookmarkletsLayer
from Products.Five import zcml
import collective.plonebookmarklets
from collective.plonebookmarklets.browser import BookmarkletsView


class testGetBookmarkletsSites(PloneBookmarkletsTestCase):


    def test_get_sites(self):
        self.setRoles(['Manager',])
        folder = getattr(self.portal,self.portal.invokeFactory('Folder','test-folder'),None)        
        self.setRoles(['Member',])

        view = BookmarkletsView(folder,self.app.REQUEST)
        portal_props = self.portal.portal_properties
        bm_props = portal_props.bookmarklets_properties
        assert len(view.getSites()) == len(bm_props.getProperty('available_sites')), "PloneBookmarklets, getSites() failed"


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(testGetBookmarkletsSites))
    suite.layer = IPloneBookmarkletsLayer
    return suite

