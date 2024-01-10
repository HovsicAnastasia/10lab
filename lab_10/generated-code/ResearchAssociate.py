#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Institute
import Project
import Employee

class ResearchAssociate(Employee):
	def __init__(self):
		self._fieldOfStudy = None
		"""@AttributeType string"""
		self._unnamed_Institute_ = []
		"""@AttributeType Institute*
		# @AssociationType Institute[]
		# @AssociationMultiplicity 1..*"""
		self._unnamed_Project_ = []
		"""@AttributeType Project*
		# @AssociationType Project[]
		# @AssociationMultiplicity 0..*"""

