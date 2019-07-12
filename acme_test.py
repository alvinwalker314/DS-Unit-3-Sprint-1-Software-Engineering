#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)
    
    def test_legal_names(self):
        products = generate_products()
        new_adj = [product[0].split()[0] for product in products]
        new_nouns = [product[0].split()[1] for product in products]
        new_adj = list(dict.fromkeys(new_adj))
        new_nouns = list(dict.fromkeys(new_nouns))
        for value in new_adj:
            self.assertIn(value, ADJECTIVES)
        for value in new_nouns:
            self.assertIn(value, NOUNS)


if __name__ == '__main__':
    unittest.main()

