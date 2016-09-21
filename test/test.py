# -*- coding: utf-8 -*-
import random


def mkLife(n, d):
	s = d

	def f(s = 3):
		lst = range(n)
		random.shuffle(lst)
		print 98
		print s
		return lst
	print f(s)
	print 108
	return f()
s = mkLife(9,2)
print s
