#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Calculadora(object):
    def __init__(self, num=None):
        if num is None:
            self._num = int(0)
        else:
            self._num = int(num)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b

    def is_even(self):
        return (self._num % 2 == 0)

    @staticmethod
    def is_odd(a):
        # return bool(a - ((a>>1)<<1))
        return bool(a & 1)
