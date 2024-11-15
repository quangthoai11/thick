# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:44:59 2024

@author: Admin
"""

def question_1(n: int) -> bool:
 if n <=1:
     return False
 for i in range(2,n):
     if n % i==0:
         return False
 return True
print(question_1(11))
print(question_1(4))



