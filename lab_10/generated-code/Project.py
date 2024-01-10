#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ResearchAssociate

class Project(object):
	def __init__(self):
		self._name = None
		"""@AttributeType string"""
		self._start = None
		"""@AttributeType Date"""
		self._end = None
		"""@AttributeType Date"""
		self._unnamed_ResearchAssociate_ = []
		"""@AttributeType ResearchAssociate*
		# @AssociationType ResearchAssociate[]
		# @AssociationMultiplicity 1..*"""

