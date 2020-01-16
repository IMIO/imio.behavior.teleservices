# -*- coding: utf-8 -*-

from plone import api
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form.browser.select import SelectWidget
from z3c.form.interfaces import ISelectWidget
from zope.interface import implementer


class ISelectProcedureWidget(ISelectWidget):
    """Marker interface for the SelectProcedureWidget"""


@implementer(ISelectProcedureWidget)
class SelectProcedureWidget(SelectWidget):
    noconfig_template = ViewPageTemplateFile("browser/templates/no_config.pt")
    badconfig_template = ViewPageTemplateFile("browser/templates/bad_config.pt")
    display = ViewPageTemplateFile('browser/templates/select_display.pt')

    def update(self):
        super(SelectProcedureWidget, self).update()

    def render(self):
        # import ipdb;ipdb.set_trace()
        url = api.portal.get_registry_record("procedures.url_formdefs_api")
        if not url or url == "":
            return self.noconfig_template(self)
        elif self.items is not None and len(self.items) <= 1:
            return self.badconfig_template(self)
        else:
            return self.display(self)
            # return super(SelectProcedureWidget, self).render()


# from z3c.form.interfaces import NOVALUE
# self.extract() == NOVALUE
# this is True if we can choose a NOVALUE items in select =>
