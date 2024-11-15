# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:02:30 2024

@author: Admin
"""

def question_16(*args) -> float:
    if not args:
        return None
    trungbinh=sum(args)/len(args)
    return trungbinh
print(question_16(1,2,3,4,5))
print(question_16(10,20))
print(question_16())
