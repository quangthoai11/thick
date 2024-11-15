# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:36:34 2024

@author: Admin
"""
from typing import Optional, List
def question_10() -> Optional[List[int]]:
    ds=input("nhập vào ds")
    if not ds :
        return None
    dssonguyen=[int(i) for i in ds.split()]
    return dssonguyen



