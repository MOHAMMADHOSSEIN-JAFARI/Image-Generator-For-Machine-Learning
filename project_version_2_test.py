# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 02:00:31 2022

@author: unimi
"""
from project_version_2 import *
import unittest
class Testproject(unittest.TestCase):
     def test(self):
        self.assertRaises(TypeError, vorarr, True)
        
       