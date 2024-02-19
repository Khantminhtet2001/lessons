num=435
count=2
def function(num):
    while num==0:
        count+=1;
        num>>=2
    return num
    


# print(function())
print(count)