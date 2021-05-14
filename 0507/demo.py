import numpy as np
import random

a = np.array([1, 2, 3, 4])     #一維陣列建立
b = np.array([(2.5, 1, 3, 4.5), (5, 6, 7, 8)], dtype = float)  #二維陣列建立
c = np.array([[(2.5, 1, 3, 4.5), (5, 6, 7, 8)], [(2.5, 1, 3, 4.5), (5, 6, 7, 8)]], dtype = float)  #三維陣列建立

x1 = np.zeros((2, 3), dtype = int)               # 建立一個2x3全為0的陣列
x2 = np.ones((2, 3, 4))             # 建立一個2x3x4全為1的陣列
x3 = np.arange(1, 10, 2)            # 建立一個由1開始，不超過10，間隔值為2的均勻數值陣列
x4 = np.linspace(0, 10, 5)          # 建立一個0到10之間，均勻的5個數值陣列
x5 = np.full((3,2), 8)              # 建立一個3x2全為8的陣列
x6 = np.eye(2)                      # 建立一個5x5的單位矩陣
x7 = np.random.random((2,3))        # 建立一個2x3的隨機值矩陣
x8 = np.random.randint(2,135,(2,3))        
x8 = x8.reshape(1,6)
x9 = np.random.shuffle(x8)

filename = "out2.npy"
with open(filename, "wb") as fp:
    np.save(fp, x4)

print("************************")

data = list("This is a book")
random.shuffle(data)
print("".join(data))



# a = numpy.array([1,1,1])
# # 一維
# b = numpy.array([(2,2,2),(2,2,2)], dtype = int)
# # 二維
# c = numpy.array([[(3,3,3),(3,3,3),(3,3,3)],[(3,3,3),(3,3,3),(3,3,3)]], dtype = int)
# # 三維

print(x9)

