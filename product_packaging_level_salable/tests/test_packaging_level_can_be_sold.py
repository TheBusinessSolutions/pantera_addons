# Copyright 2023 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo.exceptions import ValidationError

from .common import Common


class TestPackagingLevelCanBeSold(Common):
    @classmethod
    def setUpClassSaleOrder(cls):
        super().setUpClassSaleOrder()
        cls.order_line.product_uom_qty = 3.0
        # Needed for W8110 of pylint-odoo.
        return None

    def test_packaging_level_can_be_sold(self):
        self.order_line.write({"product_packaging_id": self.packaging_tu.id})
        exception_msg = (
            "Packaging Test packaging cannot be sold on product {} must be set "
            "as 'Sales' in order to be used on a sale order."
        ).format(self.product.name)
        with self.assertRaisesRegex(ValidationError, exception_msg):
            self.order_line.write(
                {"product_packaging_id": self.packaging_cannot_be_sold.id}
            )

    def test_onchange_product_packaging_id(self):
        self.order_line.write({"product_packaging_id": self.packaging_tu.id})
        result = self.order_line._onchange_product_packaging_id()
        self.assertIn("warning", result)

    def test_product_packaging_can_be_sold(self):
        """Check that a product.packaging can be independently set as can be sold."""
        exception_msg = (
            "Packaging Test packaging cannot be sold on product {} must be set "
            "as 'Sales' in order to be used on a sale order."
        ).format(self.product.name)
        with self.assertRaisesRegex(ValidationError, exception_msg):
            self.order_line.write(
                {"product_packaging_id": self.packaging_cannot_be_sold.id}
            )
        # Packaging can be sold even if the packaging level does not allows it
        self.packaging_cannot_be_sold.sales = True
        self.order_line.write(
            {"product_packaging_id": self.packaging_cannot_be_sold.id}
        )
        # Changing the packaging level on product.packaging updates can_be_sold
        self.salable_packagings.unlink()
        self.packaging_cannot_be_sold.packaging_level_id = self.packaging_level_tu
        self.packaging_cannot_be_sold.packaging_level_id = (
            self.packaging_level_cannot_be_sold
        )
        self.assertEqual(self.packaging_cannot_be_sold.sales, False)
        # Changing the can_be_sold on the packaging_level does not update the packaging
        self.packaging_level_cannot_be_sold.can_be_sold = True
        self.assertEqual(self.packaging_cannot_be_sold.sales, False)
