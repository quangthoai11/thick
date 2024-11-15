# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:48:53 2024

@author: Admin
"""

import random
def question_12() -> bool:
    n=random.randint(1,1000)
    print(f"Số ngẫu nhiên là {n}")
    if n<=1:
        return False
    for i in range (2,n):
        if n % i ==0 :
            return False
    return True
print (question_12())
    