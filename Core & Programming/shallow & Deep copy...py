l=[10,20,30,40,50]
m=l
print(l)
print(m)
l[2]=60
print(l)
print(m)

l=[10,20,30,40,50]
import copy
l1=copy.copy(l)
print('l:',l)
print('l1:',l1)
l[2]=60
print("after updating 'l'")
print('l:',l)
print('l1:',l1)
print("after updating 'l1'")
l1[2]=80
print('l:',l)
print('l1:',l1)
print('Deep copy')

l=[10,20,30,40,50]
import copy
l1=copy.deepcopy(l)
print('l:',l)
print('l1:',l1)
l[2]=60
print("after updating 'l'")
print('l:',l)
print('l1:',l1)
print("after updating 'l1'")
l1[2]=80
print('l:',l)
print('l1:',l1)

import copy
print('shallow copy')
l1=[10,[20,30],[40,50]]
l2=copy.copy(l1)
print('l1:',l1)
print('l2:',l2)
l1[1][0]=80
print('after updating l1[1][0]')
print('l1:',l1)
print('l2:',l2)
l2[2][0]=90
print('after updating l2[2][0]')
print('l1:',l1)
print('l2:',l2)

import copy
print('deep copy')
l1=[10,[20,30],[40,50]]
l2=copy.deepcopy(l1)
print('l1:',l1)
print('l2:',l2)
l1[1][0]=80
print('after updating l1[1][0]')
print('l1:',l1)
print('l2:',l2)
l2[2][0]=90
print('after updating l2[2][0]')
print('l1:',l1)
print('l2:',l2)



