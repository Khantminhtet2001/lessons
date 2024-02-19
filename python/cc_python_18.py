#map

nums=[2,5,6,7,8,9,10]


# def mapFunction(num):
#     return num*2

# print(list(map(mapFunction,nums)))

nums=[num*2 for num in nums if(num%2==0)]
print(nums);