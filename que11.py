# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:32:50 2024

@author: Admin
"""

def question_11(n: int) -> int:
    F0 = 0
    F1 = 1
    for i in range(n-1):
        Fn=F0+F1
        F0,F1=F1,Fn
    return Fn
print(question_11(10))