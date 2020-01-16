from plone.dexterity.browser.view import DefaultView

import z3c.form


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ProcedureDisplay(DefaultView):

    template = "templates/item.pt"

    def updateWidgets(self):
        super(ProcedureDisplay, self).updateWidgets()
        for widget in self.widgets.values():
            if not widget.value:
                widget.mode = z3c.form.interfaces.HIDDEN_MODE
