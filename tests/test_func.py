from unittest import TestCase

import numpy as np
from statworkshop.func import (
	cov,
	var,
	)

class test_basics(TestCase):

	def test_var_nonarray():
		non_array = np.array
		with self.assertRaises(TypeError):
			var(non_array)

	def test_var_empty():
		"""
		Test for how `var` deals with an empty list
		"""
		empty_array = np.array([])
		self.assertEqual(var(empty_array), 0.)

	def test_var_one_element_array():
		"""
		Test for how `var` deals with an empty list
		"""
		one_element_array = np.array([1.])
		self.assertEqual(var(one_element_array), 0.)

