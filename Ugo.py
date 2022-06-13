import pandas as pd
import numpy as np
import math as math
import matplotlib.pyplot as plt

# creating pythagora's triples
"""this module essentially allows you to get the last term in a pythagoras triangle given any two terms
.no other is required in imputing the numbers"""
first_num = int(input("please choose your number; remember, number can't be float: "))
second_num =int(input("please choose your number; remember, number can't be float: "))
num_list = []
check_zero=[1,first_num,second_num]
#check_negative
if all(check_zero) and first_num>0 and second_num>0:

   num_list.append(first_num)
   num_list.append(second_num)
   big_3 = num_list[0]**2 + num_list[1]**2
   # since order is not defined, the absolute difference of the two numbers is required
   small_3 = abs(num_list[0]**2 - num_list[1]**2)

   if math.sqrt(big_3)*10==10*(int(math.sqrt(big_3))):
       print(f"the third number is ",int(math.sqrt(big_3)))
   elif math.sqrt(small_3)*10==10*(int(math.sqrt(small_3))):
       print("the third number is ",int(math.sqrt(small_3)))
   else:
       print("numbers can't form pythagoras triple")
else:
    print("number can't be zero or negative")

