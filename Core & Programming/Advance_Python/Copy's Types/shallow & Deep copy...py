# l=[10,20,30,40,50]
# m=l
# print(l)
# print(m)
# l[2]=60
# print(l)
# print(m)
#
# l=[10,20,30,40,50]
# import copy
# l1=copy.copy(l)
# print('l:',l)
# print('l1:',l1)
# l[2]=60
# print("after updating 'l'")
# print('l:',l)
# print('l1:',l1)
# print("after updating 'l1'")
# l1[2]=80
# print('l:',l)
# print('l1:',l1)
# print('Deep copy')
#
# l=[10,20,30,40,50]
# import copy
# l1=copy.deepcopy(l)
# print('l:',l)
# print('l1:',l1)
# l[2]=60
# print("after updating 'l'")
# print('l:',l)
# print('l1:',l1)
# print("after updating 'l1'")
# l1[2]=80
# print('l:',l)
# print('l1:',l1)
#
# import copy
# print('shallow copy')
# l1=[10,[20,30],[40,50]]
# l2=copy.copy(l1)
# print('l1:',l1)
# print('l2:',l2)
# l1[1][0]=80
# print('after updating l1[1][0]')
# print('l1:',l1)
# print('l2:',l2)
# l2[2][0]=90
# print('after updating l2[2][0]')
# print('l1:',l1)
# print('l2:',l2)
#
# import copy
# print('deep copy')
# l1=[10,[20,30],[40,50]]
# l2=copy.deepcopy(l1)
# print('l1:',l1)
# print('l2:',l2)
# l1[1][0]=80
# print('after updating l1[1][0]')
# print('l1:',l1)
# print('l2:',l2)
# l2[2][0]=90
# print('after updating l2[2][0]')
# print('l1:',l1)
# print('l2:',l2)


# d={}
# d[1]=1
# d[2]=2
# d[3]=3
# d[4]=4
# d[5]=5
# print(d)
# for i in d:
#     d[i]={}
# print(d)
# d[1]['Name']='Aadhya'
# d[1]['village']='kkd'
# d[2]['Name']='Shiva'
# d[2]['village']='srikakulam'
# d[3]['Name']='sathwik'
# d[3]['village']='hyd'
# d[4]['Name']='Parul'
# d[4]['village']='vizag'
# d[5]['Name']='Aditya'
# d[5]['village']='Rjy'
# print('d:',d)
# d1=d
# print('d1:',d1)
# print("After changing d1[5]['village']='kkd' ")
# d1[5]['village']='kkd'
# print('d:',d)
# print('d1:',d1)
# print("After changing d d[3]['village']='Ongole'")
# d[3]['village']='Ongole'
# print('d:',d)
# print('d1:',d1)


import copy
# print('Shallow copy in nested')
# print('d:',d)
# d1=d.copy()
# print('d1:',d1)
# print('id(d1)--',id(d))
# print('id(d1)--',id(d1))
# print()
# print('In nested ')
# print('d:',id(d[1]['Name']))
# print('d1:',id(d1[1]['Name']))
# print()
# print("After changing d1[5]['village']='kkd' ")
# d1[5]['village']='kkd'
# print('d:',d)
# print('d1:',d1)
# print("After changing d d[3]['village']='Ongole'")
# d[3]['village']='Ongole'
# print('d:',d)
# print('d1:',d1)
# print()
# print('Deep copy')
# print()
# print('d:',d)
# d1=copy.deepcopy(d)
# print('d1:',d1)
# print('id(d1)--',id(d))
# print('id(d1)--',id(d1))
# print()
# print('In nested ')
# print(id(d[1]))
# print(id(d1[1]))
# print(id(d[1])==id(d1[1]))
# print()
# print("After changing d1[5]['village']='kkd' ")
# d1[5]['village']='kkd'
# print('d:',d)
# print('d1:',d1)
# print("After changing d d[3]['village']='Ongole'")
# d[3]['village']='Ongole'
# print('d:',d)
# print('d1:',d1)

