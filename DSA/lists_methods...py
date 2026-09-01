# '''split()'''
# s='aditya Shiva Satwik hemanth'
# r=s.split()
# print(r)
# s='aditya-Shiva-Satwik-hemanth'
# r=s.split('-')
# print(r)
# s='adi,tya,Shiv,a,Sat,wik,hem,anth'
# r=s.split(',')
# print(r)
# s='adi,tya,Shiv,a,Sat,wik,hem,anth'
# r=s.split()
# print(r)
# '''capitalise()'''
# c='aditya Hemanth Sathwik Shiva'
# print(c)
# c=c.capitalize()
# print(c)
# c='Aditya hemanth sathwik shiva'
# c=c.capitalize()
# print(c)
# c = 'adiTya hemAnth sathwik shiva'
# c = c.capitalize()
# print(c)
# '''lower()'''
# s='Aditya Hemanth Shiva Sathwik'
# s=s.lower()
# print(s)
# s='Aditya@Hem45anth Shiva Sathwik'
# s=s.lower()
# print(s)
# s='Aditya@Hem45aNth+Shiva Sathwik'
# s=s.lower()
# print(s)
# '''upper()'''
# s='Aditya#Hemanth@Shiva'
# s=s.upper()
# print(s)
# s='Aditya#Hem49anth@Shiva'
# s=s.upper()
# print(s)
# '''swapcase()'''
# s=""
# s=s.swapcase()
# print(s)
# s="AdityaHemanthShiva4587@#$"
# s=s.swapcase()
# print(s)
# '''title()'''
# s=''
# s=s.title()
# print(s)
# s='AdityaHemanthShiva'
# s=s.title()
# print(s)
# s='Aditya hemanth shiva'
# s=s.title()
# print(s)
# s='Aditya @hemanth$shiva'
# s=s.title()
# print(s)
# '''count(string, start, end)'''
# s='dfghjkasdfgjhgfsdfg'
# print(s.count('d'))
# s='dfghjkasdfgjhgfsdfg'
# print(s.count('d',0,8))
# s='dfghjkasdfgjhgfsdfg'
# print(s.count('d',0,9))
# s='dfghjkasdfgjhgfsdfg'
# print(s.count('d',5,-1))
# s='dfghjkasdfgjhgfsdfg'
# print(s.count('d',-5,1))
# '''find(string, start, end)'''
# s='asdffdsalkjhtyu'
# print(s.find('d'))
# s='asdffdsalkjhtyu'
# print(s.find('d',4,-1))
# s='asdffdsalkjhtyu'
# print(len(s))
# print(s.find('d',4,-1))
# s='asdffdsalkjhtyu'
# print(s.find('d',-4,1))
# s='asdffdsalkjhtyu'
# print(s.find('d',-1,14))
# print()
# '''rfind(string, start, end)'''
# s='asdffdsalkjhtyu'
# print(s.rfind('d'))
# s='asdffdsalkjhtyu'
# print(s.rfind('d',4,-1))
# s='asdffdsalkjhtyu'
# print(len(s))
# print(s.rfind('d',4,-1))
# s='asdffdsalkjhtyu'
# print(s.rfind('d',-4,1))
# s='asdffdsalkjhtyu'
# print(s.rfind('d',-1,14))
# '''index(string, start, end)'''
# s='asdfgerhasd'
# print(s.index('a'))
# s='asdfgerhasd'
# print(s.index('g'))
# s='asdfgerhasd'
# print(s.index('a',1,len(s)))
# s='asdfgerhasd'
# # print(s.index('a',-1,-len(s)))
# print()
# '''rindex(string, start, end)'''
# s='asdfgerhasd'
# print(s.index('a'))
# s='asdfgerhasd'
# print(s.index('g'))
# s='asdfgerhasd'
# print(s.index('a',1,len(s)))
# s='asdfgerhasd'
# # print(s.index('a',-1,-len(s)))
# print()
# '''endswith(string)'''
# s='sdfgqer'
# print(s.endswith('r'))
# print(s.endswith('r',len(s),2))
# '''startswith(string)'''
# s='wertyui'
# print(s.startswith('s'))
# print(s.startswith('w'))
# print(s.startswith('w',2,len(s)))
# '''isalnum()'''
# s='12345678'
# print(s.isalnum())
# s='1234567fgh8'
# print(s.isalnum())
# s='1234567dfgh@#$8'
# print(s.isalnum()
# '''isalpha()'''
# s='asAdfg'
# print(s.isalpha())
# s='asdf345g'
# print(s.isalpha())
# s='asdf@$Ag'
# print(s.isalpha())
'''isdecimal()'''
# '''isdigit()'''
# s='234567'
# print(s.isdigit())
# s='23A4567'
# print(s.isdigit())
# s='234@567'
# print(s.isdigit())
# '''islower()'''
# s='sdfgh'
# print(s.islower())
# s='sdAfgh'
# print(s.islower())
# '''isupper()'''
# s='asdfgh'
# print(s.isupper())
# s='asDfgh'
# print(s.isupper())
# s='23456'
# print(s.isupper())
# s='ASDFG'
# print(s.isupper())
'''isspace()'''
s='df sdfg sdf'
print(s.isspace())

'''replace(old, new)

strip()
rstrip()
lstrip()
removeprefix(string)
removesuffix(string)

join(iterbale)

format(parameter values)'''
