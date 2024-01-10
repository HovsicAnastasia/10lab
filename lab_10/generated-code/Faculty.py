#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Employee
import Institute

class Faculty(object):
	def __init__(self):
		self._name = None
		"""@AttributeType string"""
		self._dean = None
		"""@AttributeType Employee
		# @AssociationType Employee
		# @AssociationMultiplicity 1"""
		self._unnamed_Institute_ = []
		"""@AttributeType Institute*
		# @AssociationType Institute[]
		# @AssociationMultiplicity 1..*
		# @AssociationKind Composition"""

