#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
import Faculty

class Employee(object):
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self):
		self._ssNo = None
		"""@AttributeType int"""
		self._name = None
		"""@AttributeType string"""
		self._email = None
		"""@AttributeType string"""
		self._counter = None
		"""@AttributeType int"""
		self._leads = None
		"""@AttributeType Faculty
		# @AssociationType Faculty
		# @AssociationMultiplicity 0..1"""

