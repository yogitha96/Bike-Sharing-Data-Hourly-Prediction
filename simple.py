import numpy as np

inp = input().split()
for i in inp:
    if i.isdigit():
        print("YEs")
    elif i.isalpha():
        print("No")
    else:
        print("why")
    
   