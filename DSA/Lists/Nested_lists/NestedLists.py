'''Column Wise Transversing'''
# r=int(input('Enter No of Rows: '))
# nl=[]
# for i in range(r):
#     nl.append(list(map(int,input().split())))
# # print(nl) # [[10, 20, 30, 40],
# #              [50, 60, 70, 80],
# #              [90, 100, 110, 120],
# #              [130, 140, 150, 160]]
# for i in range(0,len(nl)):
#     for j in range(0,len(nl[0])):
#         print(nl[j][i],end=" ")
#     print()


# r=int(input('Enter No of Rows : '))
# c=int(input('Enter No of Columns : '))
# nl=[]
# for i in range(r):
#     l=[]
#     for j in range(c):
#         l.append(int(input()))
#     nl.append(l)
# # print(nl) # [[10, 20, 30, 40],
# #              [50, 60, 70, 80],
# #              [90, 100, 110, 120]]
# r=3
# c=4

'''Diagonal Elements'''
# nl=[[10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130,140,150,160]]
# # for i in range(c):
# #     for j in range(r):
# #         # print(j,i,end="    ")
# #         print(nl[j][i],end="   ")
# #     print()
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         if i==j:
#             print(1,end=" ")
#             # print(nl[i][j],end=" ")
#         # elif i+j==(len(nl)-1):
#         #     print(nl[i][j],end=" ")
#         else:
#             print(0,end=" ")
#     print()
'''Neighbour & Sourrounding Elements '''

'''Straight Elements'''
# r=int(input('Enter of Rows: '))
# nl=[]
# for i in range(r):
#     nl.append(list(map(int,input().split())))
# nl=[[10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130,140,150,160]]
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         print(nl[i][j],end="->")
#         if i!=0:
#             print(nl[i-1][j],end=" ")
#         if j!=(len(nl[i])-1):
#             print(nl[i][j+1],end=" ")
#         if i!=(len(nl)-1):
#             print(nl[i+1][j],end=' ')
#         if j!=0:
#             print(nl[i][j-1],end=' ')
#         print()
#
# print('-'*50)
# '''Straight Elements & it's sum'''
# nl=[[10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130,140,150,160]]
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         sum=0
#         print(nl[i][j],end="->")
#         if i!=0:
#             sum+=nl[i-1][j]
#         if j!=(len(nl[i])-1):
#             sum+=nl[i][j+1]
#         if i!=(len(nl)-1):
#             sum+= nl[i+1][j]
#         if j!=0:
#             sum+=nl[i][j-1]
#         print(sum)
# print('-'*50)
#
# '''Corner Elements'''
# nl=[[10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130,140,150,160]]
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         print(nl[i][j],end="->")
#         if i!=0 and j!=0:
#             print(nl[i-1][j-1],end=" ")
#         if j!=(len(nl[i])-1) and i!=0:
#             print(nl[i-1][j+1],end=" ")
#         if i!=(len(nl)-1) and j!=(len(nl[i])-1):
#             print(nl[i+1][j+1],end=' ')
#         if j!=0 and i!=(len(nl)-1):
#             print(nl[i+1][j-1],end=' ')
#         print()
# print('-'*50)
#
# '''Corner Elements and its sum'''
# nl=[[10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130,140,150,160]]
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         sum=0
#         print(nl[i][j],end="->")
#         if i!=0 and j!=0:
#             sum+=nl[i-1][j-1]
#         if j!=(len(nl[i])-1) and i!=0:
#             sum+=nl[i-1][j+1]
#         if i!=(len(nl)-1) and j!=(len(nl[i])-1):
#             sum+=nl[i+1][j+1]
#         if j!=0 and i!=(len(nl)-1):
#             sum+=nl[i+1][j-1]
#         print(sum)
#
# print('-'*50)


'''Island Perimeter
    Consider  -- 0 as Water & 1 as Land'''
l=[
    [0,1,1,1],
    [0,1,0,0],
    [1,1,1,0],
    [0,0,1,0]
]
l=[
    [0,1,0],
    [0,0,0],
    [0,1,0]]
p=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j]==1:
            if i==0 or l[i-1][j]==0:
                p+=1
            if i==len(l)-1 or l[i+1][j]==0:
                p+=1
            if j==0 or l[i][j]==0:
                p+=1
            if j==len(l[i])-1 or l[i][j+1]==0:
                p+=1
print(p)










































































































