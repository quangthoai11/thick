# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 01:37:54 2024

@author: Admin
"""

import random
from typing import Tuple
def question_2(n: int) -> Tuple[int, float]:
  ds=[]
  for i in range(n):
     x=random.randint(1,100)
     ds.append(x)
  tong=sum(ds)
  trungbinh=tong / n
  return(tong,trungbinh)



 