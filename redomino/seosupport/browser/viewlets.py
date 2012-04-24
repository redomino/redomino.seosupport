from cgi import escape
from zope.component import getMultiAdapter
from Products.CMFPlone.utils import safe_unicode
from plone.app.layout.viewlets.common import TitleViewlet as BaseViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class TitleViewlet(BaseViewlet):

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_portal_state')
        context_state = getMultiAdapter((self.context, self.request),
                                         name=u'plone_context_state')
        page_title = escape(safe_unicode(context_state.object_title()))
        portal_title = escape(safe_unicode(portal_state.navigation_root_title()))
        if page_title == portal_title:
            self.site_title = portal_title
        else:
            self.site_title = u"%s &mdash; %s" % (portal_title, page_title)
