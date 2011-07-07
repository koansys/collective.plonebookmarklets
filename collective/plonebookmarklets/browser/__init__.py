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

from Products.Five.browser import BrowserView
from zope.component import getUtility
from zope.interface import implements
from urlparse import urlsplit
from xml.dom import minidom
from string import split, find


class BookmarkletsView(BrowserView):
    """ Render the bookmarklets view """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.props = self.context.portal_url.portal_properties.bookmarklets_properties

    def getSites(self):
        """ returns bookmarking sites. """
        if self.context.Type() != 'Plone Site':
            page = self.context.aq_inner.aq_parent
        else:
            page = self.context
        page_url = page.absolute_url()
        page_title = page.title.replace(' ', '+')
        page_descr = page.Description()
    
        
        displayed_sites = []
        sites = []       
    
        displayed_sites = self.props.displayed_sites 
    
        for x in displayed_sites: 
            sites.append(getattr(self.props, x)) 
        return sites

