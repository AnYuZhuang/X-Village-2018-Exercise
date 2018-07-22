#Lesson05-String  Ex1 排版九九乘法表
RANGE1 = [1, 3]
RANGE2 = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]
import math
for i in range(RANGE1[0], RANGE1[1] + 1):         #i取1~3
    for j in range(RANGE2[0], RANGE2[1] + 1):     #j取1~9
        for k in calc(i, j):
         print('{0:^2}{1:^2}{2:^2}={3:>2}{4:>2}'.format(i,'*',j,k['result'],"|"),end='')
    print("")
