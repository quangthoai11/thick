# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 01:48:37 2024

@author: Admin
"""
from typing import Tuple
def question_3(s: str) -> Tuple[int, int]:
    hoa=0
    thuong=0
    for i in s:
        if i.isupper():
            hoa+=1
        elif i.ilower():
            thuong+=1
    return(hoa,thuong)




