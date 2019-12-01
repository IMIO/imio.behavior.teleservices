# -*- coding: utf-8 -*-

from imio.behavior.teleservices import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
# from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.interface import provider


@provider(IFormFieldProvider)
class ITsProcedure(model.Schema):
    """
    """

    procedures = schema.Choice(
        vocabulary="imio.behavior.teleservices.vocabularies.remote_procedures",
        title=_(u"E-Guichet procedures"),
        required=False,
    )
