# -*- coding: utf-8 -*-

from imio.behavior.teleservices import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IProceduresControlPanel(Interface):

    url_formdefs_api = schema.TextLine(
        title=_(u'formdefs url api'),
        description=_(u'Formdefs url api'),
        required=False,
    )

    secret_key_api = schema.Password(
        title=_(u'secret key'),
        description=_(u'Secret key to use API'),
        required=False,
    )


class ProceduresControlPanelForm(RegistryEditForm):
    schema = IProceduresControlPanel
    schema_prefix = "procedures"
    label = u'Procedures Settings'


ProceduresControlPanelView = layout.wrap_form(
    ProceduresControlPanelForm, ControlPanelFormWrapper)
