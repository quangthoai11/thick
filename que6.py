# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:10:12 2024

@author: Admin
"""

def question_6(n: int) -> int:
    giaithua=1
    for i in range(1,n+1):
        giaithua*=i
    return giaithua
print(question_6(5))
print(question_6(7))
    


