myDict={
    'brand': 'Redmi',
    'model': 'Note 8 Pro',
    'year' : 2018,
    'year' : 2020,   ##duplicate not allowed
    'color': ['red','blue','green','white']
    }


for x in myDict:
    print(myDict[x])
for x in myDict.values():
  print(x)
for x in myDict.keys():
  print(x)
for x, y in myDict.items():
  print(x, y)

# myFamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
  child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myFamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myFamily)
print(myFamily["child2"]["name"])

# myDict.update({'year':200000})
# print(myDict['model'])
# print(myDict.get('year'))
# print(myDict.keys())
# print(myDict.values())

# myDict.pop('color')
# print(myDict)

# # print(myDict.popitem())
# # del myDict['model']
# # print(myDict)
# myDict.clear()
# print(myDict)


# if 'brand' in myDict:
#     print("yes,'brand' is one of the keys in the myDict dictionary")
# else:
#     print('none')
# x=myDict['model']
# y=myDict.get('model')
# z=myDict.keys()
# b=myDict.values()
# print(b)

# myDict['cpu']='Helio G 90 T'
# print(b)

# c=myDict.items()
# print(c)

# print(f'{x}\n {y}\n {z}\n')
# print(myDict)
# print(myDict['brand'])
# print(len(myDict))
# print(type(myDict))

# mySelf=dict(name="Khant Min Htet",age=22,country="myanmar")
# print(mySelf)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# a = car.keys()

# print(a) #before the change

# car["color"] = "white"

# print(a) #after the change