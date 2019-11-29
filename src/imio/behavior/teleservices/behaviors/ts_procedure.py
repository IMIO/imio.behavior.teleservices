# -*- coding: utf-8 -*-

from imio.behavior.teleservices import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
# from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class ITsProcedureMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ITsProcedure(model.Schema):
    """
    """

    procedures = schema.Choice(
            vocabulary="imio.behavior.teleservices.vocabularies.remote_procedures",
            title=_(u"E-Guichet procedures"),
            required=False,
        )


@implementer(ITsProcedure)
@adapter(ITsProcedureMarker)
class TsProcedure(object):
    def __init__(self, context):
        self.context = context
