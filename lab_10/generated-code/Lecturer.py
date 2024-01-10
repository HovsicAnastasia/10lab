#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Course
import ResearchAssociate

class Lecturer(ResearchAssociate):
	def __init__(self):
		self._unnamed_Course_ = []
		"""@AttributeType Course*
		# @AssociationType Course[]
		# @AssociationMultiplicity 1..*"""

