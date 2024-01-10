#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Faculty
import ResearchAssociate

class Institute(object):
	def __init__(self):
		self._name = None
		"""@AttributeType string"""
		self._address = None
		"""@AttributeType string"""
		self._unnamed_Faculty_ = None
		"""@AttributeType Faculty
		# @AssociationType Faculty
		# @AssociationMultiplicity 1"""
		self._unnamed_ResearchAssociate_ = []
		"""@AttributeType ResearchAssociate*
		# @AssociationType ResearchAssociate[]
		# @AssociationMultiplicity 1..*
		# @AssociationKind Aggregation"""

