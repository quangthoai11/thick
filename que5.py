# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:58:27 2024

@author: Admin
"""
from typing import Optional 
def question_5(lst: list, x: int) -> Optional[int]:
  try:
      return lst.index(x)
  except ValueError:
      return None

print(question_5([1, 2, 3, 4, 5], 3))
print(question_5([10, 20, 30, 40], 25))
