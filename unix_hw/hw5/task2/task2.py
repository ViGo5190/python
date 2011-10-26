# -*- coding: utf-8 -*-
import pymorphy
from pymorphy import get_morph

morph = get_morph('/home/vigo/dict/')
info = morph.get_graminfo(u'ВАСЯ')

print info
