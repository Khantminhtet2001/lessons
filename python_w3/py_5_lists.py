#lists

myList=['💚','💚','🤍','💙']
list1=['apple','banana','cherry']        #list allow duplicate value
list2=[1,5,7,9,3]
list3=[True,False,False]
list4=['abc',34,True,40,"male"]         #list with string,integers and boolean values
list5=list(('apple','banana','cherry'))

print(myList)
print(len(myList))
print(type(myList))
print(myList[2])
print(myList[-1])
print(myList[1:3])
print(myList[:3])
print(myList[1:])
print(myList[-3:-1])

if '💚' in myList:
    print('Yes, 💚 is in my list')

#overwrite
    
myList[1]='💛'
print(myList)

myList[1:3]='😠','😃'
print(myList)
myList.insert(0,'🐯')
print(myList)
myList.append('🙊')
print(myList)

myList.extend(list2)
print(myList)

myList.remove('💚')
print(myList)

myList.pop(1)
print(myList)

myList.pop()
print(myList)

del list1[1]
print(list1)

del list1
# print(list1)

list3.clear()
# print(list3)

for x in myList:
    print(x)


for i in range(len(myList)):
    # print(myList[2:i])
    print(myList[i])

z=0
while z < len(myList):
    print(myList[z])
    z=z+1

[print(x) for x in myList]




