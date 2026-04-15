import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

list = [1, 0, 2, 0, 4, 6]

for item in list:
    if item == 0:
        list.remove(0)
    elif item == 1:
        list.remove(1)

print(list)
