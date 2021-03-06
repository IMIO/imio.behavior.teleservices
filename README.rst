.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==========================
imio.behavior.teleservices
==========================

Plone behavior to get (and set) global E-Guichet/Teleservices configuration into a Plone Application. Expose E-Guichet procedures in a select field.

Features
--------

- Set E-Guichet global configuration in Plone Application
- Expose E-Guichet procedure in a select field


Examples
--------
    Get procedures from e-guichet API :
        https://COMMUNE-formulaires.guichet-citoyen.be/api/formdefs/
    Find procedures in website :
        http://localhost:8080/COMMUNE/ma-commune/services-communaux/accueil/demarches


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install imio.behavior.teleservices by adding it to your buildout::

    [buildout]

    ...

    eggs =
        imio.behavior.teleservices


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/imio.behavior.teleservices/issues
- Source Code: https://github.com/collective/imio.behavior.teleservices
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
