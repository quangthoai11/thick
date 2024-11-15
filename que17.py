# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:44:54 2024

@author: Admin
"""
import random
def question_17(n: int) -> list:
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    ds.sort(reverse= True)
    return ds