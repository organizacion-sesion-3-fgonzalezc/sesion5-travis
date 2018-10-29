#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from calculadora.calculadora import Calculadora


class CalculadoraTestCase(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def tearDown(self):
        del self.calc

    def test_add(self):
        result = self.calc.add(1, 2)
        self.assertEqual(3, result)

    def test_multiply(self):
        result = self.calc.multiply(5, 2)
        self.assertEqual(10, result)

    def test_division(self):
        result = self.calc.division(10, 2)
        self.assertEqual(5, result)
    
    def test_is_odd(self):
        self.assertTrue(self.calc.is_odd(5))
        self.assertFalse(self.calc.is_odd(4))

    def test_is_even(self):
        self.assertFalse(Calculadora(5).is_even())
        self.assertTrue(Calculadora(4).is_even())



if __name__ == "__main__":
    unittest.main()
