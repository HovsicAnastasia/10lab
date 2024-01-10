#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Lecturer

class Course(object):
	def __init__(self):
		self._name = None
		"""@AttributeType string"""
		self._id = None
		"""@AttributeType int"""
		self._hours = None
		"""@AttributeType float"""
		self._teaches = []
		"""@AttributeType Lecturer*
		# @AssociationType Lecturer[]
		# @AssociationMultiplicity 1..*"""

