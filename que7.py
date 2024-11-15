# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:25:56 2024

@author: Admin
"""
import random
def question_7(n: int) -> (float, float):
    ds=[]
    for i in range(n):
        x=random.uniform(0,1)
        ds.append(x)
    return max(ds),min(ds)

print(question_7(5))
print(question_7(10))