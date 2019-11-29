# -*- coding: utf-8 -*-
from imio.behavior.teleservices.behaviors.ts_procedure import ITsProcedureMarker
from imio.behavior.teleservices.testing import IMIO_BEHAVIOR_TELESERVICES_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class TsProcedureIntegrationTest(unittest.TestCase):

    layer = IMIO_BEHAVIOR_TELESERVICES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_ts_procedure(self):
        behavior = getUtility(IBehavior, 'imio.behavior.teleservices.ts_procedure')
        self.assertEqual(
            behavior.marker,
            ITsProcedureMarker,
        )
