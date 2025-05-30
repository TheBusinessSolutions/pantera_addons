==================================
Product Supplierinfo for Customers
==================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:758a25562504083467efffa076436879f36750714f9c5f482deb752f907347d9
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fproduct--attribute-lightgray.png?logo=github
    :target: https://github.com/OCA/product-attribute/tree/17.0/product_supplierinfo_for_customer
    :alt: OCA/product-attribute
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/product-attribute-17-0/product-attribute-17-0-product_supplierinfo_for_customer
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/product-attribute&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This modules allows to use supplier info structure, available in
*Inventory* tab of the product form, also for defining customer
information, allowing to define prices per customer and product.

**Table of contents**

.. contents::
   :local:

Configuration
=============

For these prices to be used in sale prices calculations, you will have
to create a pricelist with a rule with option "Based on" with the value
"Partner Prices: Take the price from the customer info on the 'product
form')".

Usage
=====

There's a new section on *Sales* tab of the product form called
"Customers", where you can define records for customers with the same
structure of the suppliers.

There's a new option on pricelist items that allows to get the prices
from the supplierinfo at the product form.

Known issues / Roadmap
======================

-  Product prices through this method are only guaranteed on the
   standard sale order workflow. Other custom flows maybe don't reflect
   the price.
-  The minimum quantity will neither apply on sale orders.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/product-attribute/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/product-attribute/issues/new?body=module:%20product_supplierinfo_for_customer%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* AvanzOSC
* Tecnativa

Contributors
------------

-  Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>
-  Aaron Henriquez <ahenriquez@forgeflow.com>
-  Miquel Raïch <miquel.raich@forgeflow.com>
-  `Tecnativa <https://www.tecnativa.com>`__:

   -  Pedro M. Baeza
   -  Sergio Teruel

-  `Komit <https://komit-consulting.com>`__:

   -  Vang Nguyen Phu

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-luisg123v| image:: https://github.com/luisg123v.png?size=40px
    :target: https://github.com/luisg123v
    :alt: luisg123v

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-luisg123v| 

This module is part of the `OCA/product-attribute <https://github.com/OCA/product-attribute/tree/17.0/product_supplierinfo_for_customer>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
