#lambdas

# def add(n1,n2):
#     return n2+n2;




add=lambda n1,n2:n1+n2

print(add(4,5))


nums=[1,2,3,4,5,6,7,8,9,10]

evenNums=list(filter(lambda num: (num%2)==0,nums))

print(evenNums)


nums=list(map(lambda num:num*2,nums))

print(nums)