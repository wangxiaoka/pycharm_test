# -*- coding: utf-8 -*-

class Foo(object):
    def __init__(self, frob, frotz):
        self.frobnicate = frob
        self.frotz = frotz

class Bar(Foo):
    def __init__(self, frob, frizzle):
        super(Bar,self).__init__(frob,34)
        self.frazzle = frizzle

new = Bar("hello","world")
print new.frobnicate
print new.frazzle
print new.frotz