l=[0,1,2,3,4,5,6,7,8,9]
print("list:",l)
l=list(map(lambda x:x+1,l))
print('map:',l)
l=list(filter(lambda x:x<=5,l))
print('filter:',l)
l=list(sorted(l,key=lambda x:x%2==1))
print("sorted:",l)
# l=list(sorted(l,key=lambda x:x%2==0))
# print("sorted:",l)
from functools import reduce
l=reduce(lambda x,y:x+y,l)
print("reduce",l)
print("<","-"*50,">")

from functools import reduce
l=[0,1,2,3,4,5,6,7,8,9]
k=reduce(lambda x,y:x+y,sorted(filter(lambda x:x<=5,map(lambda x:x+1,l)),key=lambda x:x%2))
print(k)
'''filter() keeps an element if the function returns a truthy value, and
 removes it if the function returns a falsy value'''
l=[2,3,4,5,6]
k=list(filter(lambda x:x%2,l))
print(k)
m=list(filter(lambda x:x%2==0,l))
print(m)
n=list(filter(lambda x:x%4,l))
print(n)
l=[-4,-7,3,2,-8]
a=list(filter(lambda x:x>0,l))
print(a)

'''Sorted'''
l=[1,2,3,4,5,6,7,8,9,10]
k=list(sorted(l,reverse=True))
print(k)

names=["Aadhya",'parul','Shekhar','sathwik']
result=list(filter(lambda x:len(x)>5,names))
print(result)
result=list(sorted(result))
print(result)
result=list(sorted(result,key=lambda x :x.lower()))
print(result)

Students={'a':23,'b':67,'c':90,'d':75,'e':83}
passed=list(filter(lambda x:x[1]>30,Students.items()))
print(passed)

k=list(sorted(Students.items(),key=lambda x:x[1]))
print(k)
l = [
    {"name":"A","salary":50000},
    {"name":"B","salary":30000},
    {"name":"C","salary":70000},
    {"name":"D","salary":40000}
]
print(l[0]['name'])
print(l[-4])
print(l[0].items())
k=list(map(lambda x:x['salary']+(x['salary']*(10/100)),l))
print(k)
k=list(filter(lambda x:x['salary']>45000,l))
print(k)
# k=list(map(lambda x:x['name']=2,l))











# # print("<","-"*50,">")
# # l=dict()
# # # print(type(l))
# l={"name":'Aadhya',"id":1}
# # print(l)
# l['city']='kkd'
# # print(l)
# l['city']='rjy'
# # print(l)
# l.update({'email':'aditya@gmail.com','blood grp':'a+','Ph_no':93911})
# print(l)
# # for k,v in l.items():
# #     print(k,':',v,end=";")
# # print()
# # for k in l.keys():
# #     print(k,end=" ")
# # print()
# # for v in l.values():
# #     print(v,end=" ")
# l2={'f_name':'srinivas','m_name':'Lakshmi','s_name':'chinni'}
# l.update(l2)
# print(l)
# print(l.popitem())
# print(l.pop('f_name'))
# # print(l.keys())
# # print(l['f_name'])
# print(l.get('f_name','Not exist'))
# print(l.get('f_name'))
