#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, i1: int, i2: int):
        self.__i1 = i1
        self.__i2 = i2

    def _get_i1(self) -> int:
        print('_get_i1')
        return self.__i1

    def _set_i1(self, value: int):
        print('_set_i1')
        self.__i1 = value

    def _get_i2(self) -> int:
        print('_get_i2')
        return self.__i2

    def _set_i2(self, value: int):
        print('_set_i2')
        self.__i2 = value

    i1 = property(_get_i1, _set_i1)
    i2 = property(_get_i2, _set_i2)

    def mut(self) -> int:
        return self.__i1 * self.__i2


p = Pair(1, 2)
print(p.i1, p.i2)
p.i1 = 4
p.i2 = 5
print(p.i1, p.i2)
print(p.mut())